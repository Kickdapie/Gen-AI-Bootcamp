import asyncio
from fastapi import WebSocket
from queue_bus import get_next_todo_update


connected_clients = set()

async def handle_websocket(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            todo_update = await get_next_todo_update()
            await websocket.send_json(todo_update)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        connected_clients.remove(websocket)

async def broadcast_todo_update(data):
    for client in connected_clients:
        await client.send_json(data)