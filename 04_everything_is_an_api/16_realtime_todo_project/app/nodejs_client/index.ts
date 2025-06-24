import WebSocket from 'ws';

const ws = new WebSocket('ws://localhost:8000/ws/todos');

ws.on('open', () => {
  console.log('WebSocket connected');
});

ws.on('message', (message) => {
  console.log('Received todo update:', message);
  // Update UI or perform actions based on message
});