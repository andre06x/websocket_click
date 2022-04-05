import asyncio
import websockets

async def handler(websocket, path):

    data = await websocket.recv()

    if data =="click":
        reply = f"Data recieved as:  {data}!"
        print("chegou")

    await websocket.send("ok")

start_server = websockets.serve(handler, "localhost", 8000)

 

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()