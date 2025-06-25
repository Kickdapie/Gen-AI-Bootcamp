import asyncio
import json
import os
from aiokafka import AIOKafkaConsumer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Todo
from websocket_handler import broadcast_todo_update
from queue_bus import push_todo_update

# Define your engine (use environment variables)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@host:port/database")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Consumer logic
async def consume_todos(app, bootstrap_servers, topic):
    try:
        consumer = AIOKafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
        await consumer.start()
        print(f"Kafka consumer started for topic: {topic}")
        
        async for msg in consumer:
            try:
                todo_data = json.loads(msg.value.decode("utf-8"))
                print(f"Received todo data: {todo_data}")
                
                # Use sync session for SQLAlchemy
                with SessionLocal() as session:
                    todo = Todo(**todo_data)
                    session.add(todo)
                    session.commit()
                    print(f"Saved todo to database: {todo.id}")

                # Broadcast to WebSocket clients
                await push_todo_update(todo_data) #NEW
                await broadcast_todo_update(todo_data)
                
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
            except Exception as e:
                print(f"Error processing message: {e}")

    except Exception as e:
        print(f"Kafka consumer error: {e}")
    finally:
        try:
            await consumer.stop()
        except:
            pass

# Called at startup in app.py
async def create_todo_consumer(app, bootstrap_servers, topic):
    asyncio.create_task(consume_todos(app, bootstrap_servers, topic))
