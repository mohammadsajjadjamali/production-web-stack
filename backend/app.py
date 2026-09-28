from flask import Flask, jsonify
import os
import psycopg2
import redis

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("DB_PORT", "5432")
    )


def get_redis_connection():
    return redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        decode_responses=True
    )


@app.route("/")
def home():
    return jsonify({
        "service": "production-web-stack",
        "status": "running"
    })


@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()

        redis_client = get_redis_connection()
        redis_client.ping()

        return jsonify({
            "status": "healthy",
            "database": "connected",
            "redis": "connected"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 503


@app.route("/cache")
def cache():
    redis_client = get_redis_connection()

    redis_client.setex(
        "message",
        60,
        "Hello from Redis!"
    )

    value = redis_client.get("message")
    ttl = redis_client.ttl("message")

    return jsonify({
        "value": value,
        "ttl": ttl
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
