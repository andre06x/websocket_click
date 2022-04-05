import asyncio
from time import sleep
import websockets
import mouse 

async def handler(websocket, path):

    data = await websocket.recv()

    if data =="click":
        print("chegou")

        mouse.move(20, 120, absolute=True, duration=0.1)
        sleep(2)
        mouse.on_click(lambda: print("Left Button clicked."))

    await websocket.send("ok")

start_server = websockets.serve(handler, "localhost", 8000)

 

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()