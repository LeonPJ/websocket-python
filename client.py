import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        command = input("Enter Command: ")
        preCommand = '{"message": "register", "register":"non_ip_data"}'
        await websocket.send(preCommand)
        #print(f"(client) send to server: Jimmy")
        # name = await websocket.recv()
        #print(f"(client) recv from server {name}")

        while True:
            recvMsg = await websocket.recv()
            if recvMsg == 'stop':
                break
            else:
                print(f"recv from server {recvMsg}")


asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
