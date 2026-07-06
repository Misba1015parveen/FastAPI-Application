from pydantic import BaseModel
from datetime import datetime


class TaskCreate(BaseModel):
    title: str


class TaskResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    class Config:
        from_attributes = True