import streamlit as st
import asyncio
from websockets import connect
import json

st.title("Realtime Todo Viewer")

# Create a placeholder for live updates
todo_box = st.empty()

# Store todos in a list
todos = []

async def connect_websocket():
    async with connect("ws://localhost:8000/ws/todos") as websocket:
        while True:
            message = await websocket.recv()
            try:
                todo = json.loads(message)
                todos.append(todo)
                todo_box.write(todos)
            except Exception as e:
                st.error(f"Failed to parse message: {e}")

# Run the websocket connection in an async event loop
async def main():
    await connect_websocket()

# Run only if Streamlit supports asyncio
if __name__ == "__main__":
    asyncio.run(main())
