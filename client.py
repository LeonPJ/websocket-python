import json
import websockets
import asyncio


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        command = input('Press Enter to Excute')
        preCommand = '{"message": "register", "register":"non_ip_data"}'
        await websocket.send(preCommand)

        while True:
            recvMsg = await websocket.recv()
            if recvMsg == 'stop':
                break
            else:
                print(f'string: {recvMsg}')
                # recvMsgObj = json.loads(recvMsg)  # convert to object
                # print(recvMsgObj['data'])


asyncio.get_event_loop().run_until_complete(
    # hello('ws://192.168.5.146:9000'))
    hello('ws://127.0.0.1:9000'))
