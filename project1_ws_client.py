"""
PROJECT 1 (client): terminal chat client.
Usage:  python project1_ws_client.py <username>      (type /quit to leave)
"""
import asyncio
import json
import sys
from urllib.parse import quote

import websockets


async def main(username: str):
    uri = f"ws://127.0.0.1:8000/ws/{quote(username)}" 


    '''uri -> Variable storing the connection address.
    f"..." -> it that inserts Python expressions into a string.
    ws:// -> The WebSocket protocol without TLS encryption.
    127.0.0.1 -> The local computer, also called localhost.
    8000 -> The port where your server is listening.
    /ws/ -> The route prefix defined by the server.
    {quote(username)} -> Inserts the URL-encoded username.''' 
# use wss:// when the server runs over TLS


    async with websockets.connect(uri) as ws:

      
      '''websockets.connect(uri) -> initiates a connection to the address stored in uri.
        async with -> manages the connection's lifecycle asynchronously.
        as ws -> assigns the active connection to a variable named ws.'''
    async def reader():
            # Messages can arrive at ANY time, so we listen in a background task
            async for raw in ws:
                d = json.loads(raw)
                print(f"* {d['text']}" 
                      if d["type"] == "system"
                        else f"{d['user']}: {d['text']}")

    listener = asyncio.create_task(reader())
    try:
            while True:
                line = await asyncio.to_thread(input)    # read keyboard without blocking the listener
                '''try lets -> you handle certain errors.
                    while True -> keeps the chat running continuously.
                    input() -> waits for you to type a message.
                    asyncio.to_thread() -> runs keyboard input in a separate thread.
                    await -> waits for your input to arrive.'''
                if line.strip().lower() == "/quit":
                    break
                await ws.send(json.dumps({"text": line}))
    except (EOFError, KeyboardInterrupt):
            pass
    finally: #block runs when the program leaves the try statement.
            listener.cancel() #requests that the background message-reading task stop.


if __name__ == "__main__":
    try:
        asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "anon"))
        '''asyncio.run() -> runs the main() function in an asynchronous event loop.
        sys.argv -> a list of command-line arguments passed to the script.
        sys.argv[1] -> the first argument after the script name, which is the username.
        if len(sys.argv) > 1 else "anon" -> if no username is provided, defaults to "anon"
        
        that part is simply saying, if there were multiple arguments provided, the first argument is the username.'''
    except KeyboardInterrupt:
        pass
