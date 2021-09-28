import asyncio
import websockets
import json
import time


async def echo(websocket, path):
    print('new')
    async for message in websocket:
        #print(message,'received from client')
        # commandObj = json.loads(message)  # convert to object
        # await websocket.send(getCommand)
        # print(commandObj['message'])

        # time.sleep(3)

        # await websocket.send(commandObj['message'])
        print(data)
        await websocket.send(data)

        # time.sleep(3)

        # await websocket.send('1')
        # await websocket.send('2')
        # await websocket.send('3')

        # await websocket.send('stop')

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '127.0.0.1', 9000))
asyncio.get_event_loop().run_forever()
