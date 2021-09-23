import socket
import time
import json

jsonData = {"id": 2, "name": "abc"}

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 3333))
s.listen(5)  # maximum connect limited

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    #msg = "Welcome to the server!"
    #msg = f"{len(msg):<{HEADERSIZE}}"+msg

    #clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(1)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        # print(msg)

        clientsocket.send(bytes(msg, "utf-8"))
        # clientsocket.send(jsonData)
