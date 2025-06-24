import asyncio
from fastapi import WebSocket

connected_clients = set()

async def handle_websocket(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            # Keep connection alive and wait for messages
            data = await websocket.receive_text()
            # Echo back for testing
            await websocket.send_text(f"Received: {data}")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        connected_clients.remove(websocket)

async def broadcast_todo_update(data):
    """Broadcast todo updates to all connected WebSocket clients"""
    disconnected_clients = set()
    for client in connected_clients:
        try:
            await client.send_json(data)
        except Exception as e:
            print(f"Failed to send to client: {e}")
            disconnected_clients.add(client)
    
    # Remove disconnected clients
    connected_clients.difference_update(disconnected_clients)