# FastAPI Production Deployment

## Project Overview

This project is a simple FastAPI application deployed using Docker and Docker Compose. The application uses PostgreSQL as the database, Redis for caching, and NGINX as a reverse proxy. The project is deployed on an AWS EC2 Ubuntu server with automatic deployment using GitHub Actions.

---

## Technologies Used

- FastAPI
- Python 3.12
- Docker
- Docker Compose
- PostgreSQL
- Redis
- NGINX
- GitHub Actions
- AWS EC2
- Ubuntu

---

## Services

The application consists of the following services:

- FastAPI Application
- PostgreSQL Database
- Redis
- NGINX Reverse Proxy

---

## Features

- Dockerized FastAPI application
- Docker Compose setup
- PostgreSQL database
- Redis service
- NGINX reverse proxy
- Health Check endpoint
- Logging
- Environment variables
- Automatic deployment using GitHub Actions
- AWS EC2 deployment

---

## Running the Project Locally

Clone the repository.

```
git clone <repository-url>
```

Move inside the project.

```
cd FastAPI-Application
```

Start all services.

```
docker compose up --build
```

Open:

```
http://localhost/docs
```

Health Check:

```
http://localhost/health
```

---

## Deployment

The application is deployed on an AWS EC2 Ubuntu server.

Deployment is automated using GitHub Actions.

Whenever code is pushed to the **main** branch, GitHub Actions automatically:

- Connects to the EC2 server
- Pulls the latest code
- Rebuilds Docker containers
- Restarts the application

---

## Environment Variables

Environment variables are stored in the `.env` file.


## Health Check

Health endpoint:

```
GET /health
```

Response:

```
{
  "status": "healthy"
}
```

---

## Logging

The application uses Python logging.

Logs can be viewed using:

```
docker logs <container_name>
```

---

## Security

Basic security measures implemented:

- SSH Key Authentication
- Environment variables
- NGINX Reverse Proxy
- Docker isolated services

---

## SSL

A document named `SSL_SETUP.md` explains how HTTPS can be configured when a domain is available.

Since this project does not use a custom domain, SSL was documented instead of implemented.

---
## Firewall (UFW)

The Ubuntu Firewall (UFW) was configured to allow only the required ports.

Allowed ports:

- SSH (22)
- HTTP (80)

Commands used:

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80
sudo ufw enable
sudo ufw status

## Fail2Ban

Fail2Ban was installed on the EC2 server to provide basic protection against SSH brute-force attacks by blocking IP addresses after repeated failed SSH login attempts.

### Installation

```bash
sudo apt install fail2ban -y
```

### Enable and Start Fail2Ban

```bash
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

### Verify Status

```bash
sudo systemctl status fail2ban
```

Fail2Ban runs as a background service and helps secure the EC2 server from brute-force SSH attacks.
