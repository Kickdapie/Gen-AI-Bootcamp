import uvicorn
from fastapi import FastAPI, WebSocket, Depends, HTTPException
from sqlalchemy.orm import sessionmaker
from kafka_consumer import create_todo_consumer
from models import Todo, TodoSchema
from sqlalchemy import create_engine
from typing import List
import websocket_handler
from sqlalchemy.orm import Session
from pydantic import BaseModel
import os

app = FastAPI()

# Database setup (replace with your credentials)
DATABASE_URL = "postgresql://neondb_owner:npg_7ELNpgVKu4HQ@ep-plain-bar-a8qj9hxh-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Kafka consumer setup (replace with your Kafka server details)
bootstrap_servers = "localhost:8000"
topic = "todos"

@app.on_event("startup")
async def startup_event():
    await create_todo_consumer(app, bootstrap_servers, topic)

# WebSocket endpoint
@app.websocket("/ws/todos")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_handler.handle_websocket(websocket)

@app.get("/todos", response_model=List[TodoSchema])
async def get_todos(session: Session = Depends(get_db)):
    return session.query(Todo).all()
