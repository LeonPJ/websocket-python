import socket
import json

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)
UDPServerSocket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)  # Create a datagram socket
UDPServerSocket.bind((localIP, localPort))  # Bind to address and ip
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    messageStr = message.decode(encoding="ASCII")  # convert string
    print(f'Message from UDP Client: {messageStr}')
    UDPServerSocket.sendto(message, address)  # Sending a reply to client
    print(f'Message Send UDP Client: {messageStr}')
