import asyncio
from time import sleep
import websockets
import pyautogui

async def handler(websocket, path):

    data = await websocket.recv()
    if data =="video_click":
        print("chamou")
        
        #windows y = 30, linux = 50
        pyautogui.moveTo(50, 30)
        
        sleep(2)
        pyautogui.click()
        await websocket.send("ok")

start_server = websockets.serve(handler, "localhost", 8000)

 
asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()