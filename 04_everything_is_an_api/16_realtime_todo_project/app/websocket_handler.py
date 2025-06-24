import asyncio
from fastapi import WebSocket

connected_clients = set()
todo_update_queue = asyncio.Queue()

async def get_next_todo_update():
    return await todo_update_queue.get()

async def handle_websocket(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            # Receive todo updates from broadcast function
            todo_update = await get_next_todo_update()  # Implement this function
            await websocket.send_json(todo_update)
    except websockets.ConnectionClosed:
        connected_clients.remove(websocket)


async def broadcast_todo_update(data):
    await todo_update_queue.put(data)
    for client in connected_clients:
        await client.send_json(data)