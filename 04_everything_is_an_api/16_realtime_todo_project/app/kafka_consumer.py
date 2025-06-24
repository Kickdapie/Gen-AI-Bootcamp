import asyncio
import json
from aiokafka import AIOKafkaConsumer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Todo
from websocket_handler import broadcast_todo_update

# Define your engine (should match app.py)
DATABASE_URL = "postgresql://user:password@postgres:5432/database"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Consumer logic
async def consume_todos(app, bootstrap_servers, topic):
    consumer = AIOKafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
    await consumer.start()
    try:
        async for msg in consumer:
            todo_data = json.loads(msg.value.decode("utf-8"))
            
            # ✅ Use sync session for SQLAlchemy
            with SessionLocal() as session:
                todo = Todo(**todo_data)
                session.add(todo)
                session.commit()

            # ✅ Broadcast to WebSocket clients
            await broadcast_todo_update(todo_data)

    finally:
        await consumer.stop()

#Called at startup in app.py
async def create_todo_consumer(app, bootstrap_servers, topic):
    asyncio.create_task(consume_todos(app, bootstrap_servers, topic))
