# Production Web Stack

A production-style containerized web application stack built with Docker Compose, Flask, PostgreSQL, Redis, Nginx, Prometheus, cAdvisor, and Grafana.

The project demonstrates how multiple services can be deployed, connected, monitored, and persisted using Docker Compose.

## Architecture

```text
                    Client
                       │
                       ▼
                    Nginx
                       │
                       ▼
                    Flask
                   /     \
                  ▼       ▼
             PostgreSQL  Redis
                  │
                  │
             Persistence
                  │
                  ▼
              Docker Volume

             Monitoring
                  │
                  ▼
              Prometheus
                  │
                  ▼
               Grafana
                  ▲
                  │
               cAdvisor
```

## Technologies

* Docker
* Docker Compose
* Python / Flask
* PostgreSQL
* Redis
* Nginx
* Prometheus
* cAdvisor
* Grafana
* Linux
* Bash

## Project Features

### Application

* Flask backend
* PostgreSQL database integration
* Redis caching
* Nginx reverse proxy
* Dockerized services
* Internal Docker networking

### Reliability

* Docker health checks
* Automatic container restart with `restart: unless-stopped`
* PostgreSQL persistent storage
* Grafana persistent storage
* Service dependency configuration

### Monitoring

* Prometheus metrics collection
* cAdvisor container metrics
* Grafana monitoring dashboard
* Container CPU usage monitoring
* Container memory usage monitoring
* Container network traffic monitoring

## Services

| Service    | Description          | Port |
| ---------- | -------------------- | ---: |
| Nginx      | Reverse proxy        |   80 |
| Flask      | Backend application  | 5000 |
| PostgreSQL | Relational database  | 5432 |
| Redis      | Cache                | 6379 |
| Prometheus | Metrics collection   | 9090 |
| cAdvisor   | Container metrics    | 8080 |
| Grafana    | Monitoring dashboard | 3001 |

The Flask, PostgreSQL, and Redis services are not directly exposed to the host. They communicate through the internal Docker network.

## Project Structure

```text
production-web-stack/
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── nginx/
│   └── nginx.conf
│
├── prometheus/
│   └── prometheus.yml
│
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Configuration

Create the environment file:

```bash
cp .env.example .env
```

Edit `.env` and configure the database credentials:

```env
POSTGRES_DB=production_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=change_me
```

> `.env` is excluded from Git to prevent sensitive credentials from being committed.

## Run the Project

Start all services:

```bash
docker compose up -d
```

Check service status:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

## Application Endpoints

Main application:

```text
http://localhost/
```

Health check:

```text
http://localhost/health
```

Redis cache test:

```text
http://localhost/cache
```

## Monitoring

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3001
```

cAdvisor:

```text
http://localhost:8080
```

The Grafana dashboard monitors:

* Container CPU usage
* Container memory usage
* Container network traffic

## Health Checks

Docker health checks are configured for the main application dependencies.

Example:

```bash
docker compose ps
```

Healthy services should show:

```text
healthy
```

The Flask health endpoint verifies connectivity to both PostgreSQL and Redis.

## Persistence

PostgreSQL uses a Docker named volume:

```text
postgres_data
```

Grafana uses a Docker named volume:

```text
grafana_data
```

This allows important data to survive container recreation.

## Testing Persistence

PostgreSQL persistence was tested by:

1. Creating a database table.
2. Inserting test data.
3. Removing the PostgreSQL container.
4. Recreating the container.
5. Verifying that the data remained available.

## Monitoring Architecture

```text
Docker Containers
       │
       ▼
    cAdvisor
       │
       ▼
   Prometheus
       │
       ▼
     Grafana
```

Prometheus collects metrics from cAdvisor, while Grafana visualizes the collected metrics through dashboards.

## Useful Commands

Check running containers:

```bash
docker compose ps
```

Check resource usage:

```bash
docker stats
```

Restart the stack:

```bash
docker compose restart
```

Stop the stack:

```bash
docker compose down
```

Start the stack again:

```bash
docker compose up -d
```

## What I Practiced

This project was built to practice real-world DevOps concepts including:

* Multi-container application deployment
* Docker networking
* Reverse proxy configuration
* Environment variables
* Database persistence
* Redis caching
* Container health checks
* Automatic container restart
* Prometheus monitoring
* cAdvisor metrics
* Grafana dashboards
* Docker Compose service orchestration


## Author

**Mehrab**

DevOps Engineer 
