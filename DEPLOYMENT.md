# Deployment Guide

## Overview

This document explains how the FastAPI application was deployed on an AWS EC2 Ubuntu server using Docker, Docker Compose, NGINX, and GitHub Actions.

---

## Prerequisites

Before starting, make sure you have:

- AWS Account
- GitHub Account
- Docker installed
- Docker Compose installed
- SSH key pair
- Git installed

---

## Step 1: Launch EC2 Instance

- Launch an Ubuntu EC2 instance.
- Choose a Free Tier eligible instance type.
- Create or use an existing key pair.
- Allow the following inbound rules:
  - SSH (Port 22)
  - HTTP (Port 80)

---

## Step 2: Connect to the EC2 Server

Connect using SSH.

```bash
ssh -i "your-key.pem" ubuntu@<EC2-Public-IP>
```

---

## Step 3: Install Docker

Update the server.

```bash
sudo apt update
```

Install Docker.

```bash
sudo apt install docker.io -y
```

Enable Docker.

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Add the current user to the Docker group.

```bash
sudo usermod -aG docker $USER
```

Log out and log in again.

---

## Step 4: Install Docker Compose

Install Docker Compose.

```bash
sudo apt install docker-compose-v2 -y
```

Verify installation.

```bash
docker compose version
```

---

## Step 5: Clone the Repository

Clone the GitHub repository.

```bash
git clone <repository-url>
```

Move inside the project.

```bash
cd FastAPI-Application
```

---

## Step 6: Start the Application

Build and start all containers.

```bash
docker compose up -d --build
```

Check running containers.

```bash
docker ps
```

---

## Step 7: Verify the Application

Open the application in a browser.

Swagger UI:

```
http://<EC2-Public-IP>/docs
```

Health Check:

```
http://<EC2-Public-IP>/health
```

---

## Step 8: Configure GitHub Actions

Create the following GitHub Secrets:

- EC2_HOST
- EC2_USER
- EC2_SSH_KEY
- PROJECT_PATH

These secrets allow GitHub Actions to connect to the EC2 server and deploy the application automatically.

---

## Step 9: Automatic Deployment

Whenever code is pushed to the **main** branch:

- GitHub Actions starts automatically.
- Connects to the EC2 server using SSH.
- Pulls the latest code.
- Rebuilds Docker containers.
- Restarts the application.

No manual deployment is required after pushing changes.

---

## Deployment Verification

The deployment is successful if:

- All Docker containers are running.
- The FastAPI application is accessible.
- The `/health` endpoint returns a healthy status.
- GitHub Actions completes successfully.