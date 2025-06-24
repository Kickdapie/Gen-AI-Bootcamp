from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

class TodoSchema(BaseModel):
    id: int
    task: str
    completed: bool

    class Config:
        orm_mode = True 

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    completed = Column(Boolean, default=False)