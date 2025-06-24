from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

class TodoSchema(BaseModel):
    id: Optional[int] = None
    task: str
    completed: bool = False

    class Config:
        orm_mode = True 

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    completed = Column(Boolean, default=False)