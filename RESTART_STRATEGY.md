# Restart Strategy

## Overview

This document explains how the application handles service restarts and recovery.

---

## Docker Restart Policy

All services use the following restart policy:

```yaml
restart: always
```

This ensures that Docker automatically restarts the containers if they stop unexpectedly.

---

## Application Restart

If the FastAPI application stops because of an error, Docker automatically restarts the container.

---

## Server Restart

If the EC2 server is restarted, Docker services can be started again using:

```bash
docker compose up -d
```

---

## Manual Restart

To restart all services manually:

```bash
docker compose restart
```

To restart a specific service:

```bash
docker compose restart fastapi
```

---

## Health Check

The application provides a health check endpoint:

```
GET /health
```

Expected response:

```json
{
  "status": "healthy"
}
```

This endpoint can be used to verify that the application is running correctly after a restart.

---

## Viewing Logs

Application logs can be checked using:

```bash
docker logs fastapi-application-fastapi-1
```

To view logs for all services:

```bash
docker compose logs
```

---

## Recovery Steps

If the application is not running:

1. Check running containers.

```bash
docker ps
```

2. Restart the services.

```bash
docker compose up -d
```

3. Check the logs for any errors.

```bash
docker compose logs
```

4. Verify the application by opening:

```
http://<EC2-Public-IP>/health
```

If the response is:

```json
{
  "status": "healthy"
}
```

the application has recovered successfully.