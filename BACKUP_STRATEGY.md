# Backup Strategy

## Overview

This document explains the backup strategy used for this project.

---

## Application Code Backup

The application source code is stored in a GitHub repository.

Every code change is pushed to GitHub, which acts as the primary backup for the application code.

---

## Database Backup

The PostgreSQL database can be backed up using the `pg_dump` command.

Example:

```bash
docker exec postgres_db pg_dump -U postgres devops_db > backup.sql
```

This command creates a SQL backup file of the database.

---

## Database Restore

To restore the database:

```bash
docker exec -i postgres_db psql -U postgres devops_db < backup.sql
```

---

## Docker Volume Backup

The PostgreSQL data is stored in a Docker volume.

The volume can be backed up regularly to prevent data loss.

---

## Configuration Backup

Important configuration files should also be backed up, including:

- docker-compose.yml
- nginx/nginx.conf
- .env.example
- GitHub Actions workflow

These files are already stored in the GitHub repository.

---

## Recommended Backup Schedule

- Application Code: Every code push (GitHub)
- Database: Daily or before major updates
- Docker Volumes: Weekly
- Configuration Files: Whenever changes are made

---

## Recovery

If the server fails:

1. Launch a new EC2 instance.
2. Clone the GitHub repository.
3. Restore the database backup.
4. Run:

```bash
docker compose up -d --build
```

The application will be available again.