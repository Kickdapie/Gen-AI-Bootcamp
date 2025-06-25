# queue_bus.py
import asyncio

# Global queue for todo updates
todo_update_queue = asyncio.Queue()

async def get_next_todo_update():
    return await todo_update_queue.get()

async def push_todo_update(update):
    await todo_update_queue.put(update)
