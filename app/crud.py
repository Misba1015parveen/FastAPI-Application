from sqlalchemy.orm import Session
from app import models


def create_task(db: Session, title: str):
    task = models.Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(models.Task).all()