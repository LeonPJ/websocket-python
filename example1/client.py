import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('127.0.0.1', 3333))
s.connect(('127.0.0.1', 3333))
data = "hello world"
s.sendall(data.encode())

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            #print("new msg len:", msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        #print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")

        # print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            #print("full msg recvd")
            print(type(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = ""
