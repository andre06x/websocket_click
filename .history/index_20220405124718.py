import asyncio
from time import sleep
import websockets
import mouse 
import pyautogui


async def handler(websocket, path):

    data = await websocket.recv()

    if data =="video_click":
        print("chegou")
        pyautogui.moveTo(50, 50)

#        mouse.move(20, 120, absolute=True, duration=0.1)
        sleep(2)
        pyautogui.click()
        await websocket.send(data)

start_server = websockets.serve(handler, "localhost", 8000)

 

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()