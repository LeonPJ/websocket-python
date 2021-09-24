import asyncio
import websockets
import time


async def echo(websocket, path):
    print('new client')
    async for message in websocket:
        print('Received: ', message)
        time.sleep(2)
        await websocket.send("1")
        time.sleep(2)
        await websocket.send("2")
        time.sleep(2)
        await websocket.send("3")
        time.sleep(2)
        await websocket.send("4")
        time.sleep(2)
        await websocket.send("5")
        #greeting = f"Hello {message}!"
        # await websocket.send(greeting)
        #print(f"> {greeting}")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
