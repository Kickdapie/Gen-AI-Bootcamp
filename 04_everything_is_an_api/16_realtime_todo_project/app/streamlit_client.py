import streamlit as st
import asyncio
from websockets import connect

async def connect_websocket():
    async with connect("ws://localhost:8000/ws/todos") as websocket:
        while True:
            todo_update = await websocket.recv()
            # Update UI based on todo_update
