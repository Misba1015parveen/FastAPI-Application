from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app import models, schemas, crud
from app.logging_config import logger
from sqlalchemy import text
import redis
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB", 0)),
    decode_responses=True
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DevOps Assignment API",
    version="1.0.0"
)
logger.info("FastAPI application started successfully.")

@app.get("/")
def home():
    logger.info("Home endpoint accessed.")
    return {"message": "Welcome to the DevOps Assignment 1"}
    

@app.get("/health")
def health():
    logger.info("Health check requested.")

    health_status = {
        "status": "healthy",
        "database": "connected",
        "redis": "connected"
    }

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception:
        health_status["status"] = "unhealthy"
        health_status["database"] = "disconnected"

    try:
        redis_client.ping()
    except Exception:
        health_status["status"] = "unhealthy"
        health_status["redis"] = "disconnected"

    return health_status


@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
     logger.info(f"Creating task: {task.title}")
     return crud.create_task(db, task.title)


@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    logger.info("Fetching all tasks.")
    return crud.get_tasks(db)
