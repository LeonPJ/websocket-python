import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        command = input("Enter Commend: ")
        preCommand = '{"message": "config_get"}'
        await websocket.send(preCommand)
        #print(f"(client) send to server: Jimmy")
        while True:
            recv = await websocket.recv()
            print(f"recv from server {recv}")

asyncio.get_event_loop().run_until_complete(
    hello('ws://192.168.5.146:9000'))
# hello('ws://localhost:8765'))
