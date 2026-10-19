"""
PROJECT 1 (server): WebSocket Chat Room
Terminal 1:   uvicorn project1_ws_server:app --reload
Terminal 2:   python project1_ws_client.py alice
Terminal 3:   python project1_ws_client.py bob       (type in either, both see it)

"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
'''
fastapi -> Creates your web application.   
WebSocket -> Represents a WebSocket connection between a client and the server.
WebSocketDisconnect -> Helps detect when a client disconnects.
'''
app = FastAPI(title="WebSocket Chat")
'''
FastAPI(title="WebSocket Chat") -> Creates a FastAPI application instance with the title "WebSocket Chat".
'''

class ConnectionManager:
    """Tracks everyone connected so we can broadcast to all."""

    def __init__(self):
        self.active: dict[WebSocket, str] = {}  # socket -> username
    '''__init__() -> Initializes the ConnectionManager instance.
    self.active -> A dictionary that maps WebSocket connections to usernames.
    '''
    async def connect(self, ws: WebSocket, username: str):
        await ws.accept()
        self.active[ws] = username

    def disconnect(self, ws: WebSocket):
        self.active.pop(ws, None)

    async def broadcast(self, message: dict):
        for ws in list(self.active):
            try:
                await ws.send_json(message)
            except Exception:  # dead connection, drop it
                self.active.pop(ws, None)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def chat(ws: WebSocket, username: str):
    await manager.connect(ws, username)
    await manager.broadcast({"type": "system", "text": f"{username} joined ({len(manager.active)} online)"})
    try:
        while True:                                   # stays open until the client leaves
            data = await ws.receive_json()            # wait for a message from THIS client
            text = str(data.get("text", ""))[:500]    # never trust client input; cap its length
            if text:
                await manager.broadcast({"type": "chat", "user": username, "text": text})
    except WebSocketDisconnect:
        manager.disconnect(ws)
        await manager.broadcast({"type": "system", "text": f"{username} left ({len(manager.active)} online)"})
