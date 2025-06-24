import asyncio
from websockets import connect

async def consume_websocket_messages():
    async with connect("ws://localhost:8000/ws/todos") as websocket:
        while True:
            todo_update = await websocket.recv()
            print(todo_update)
