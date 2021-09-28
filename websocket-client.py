from json import decoder
import websocket
import _thread
import time
import json
import socket

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def UDPClientRecv():
    try:
        bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        # address = bytesAddressPair[1]
        messageStr = message.decode(encoding="ASCII")  # convert byte to string
        # objMsg = json.loads(messageStr.replace('\'', '"')) # replice ' to "
        print(f'Message from UDP Server: {messageStr}')
    except:
        print('UPD Server No Response')


def UDPClientSend(objMsgUDPSend):  # send receive(base station) data to UPD server
    bytesToSend = str.encode(str(objMsgUDPSend))
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print(f'Message Send UDP Server: {objMsgUDPSend}')
    UDPClientRecv()


def on_message(ws, message):
    objMsg = json.loads(message)
    print(f'Message from Base Station: {message}')
    if objMsg['message'] == "register":
        print('Register Success')
    elif objMsg['message'] == "non_ip_data":
        # print(objMsg['data'])
        UDPClientSend(objMsg['data'])
    else:
        print('Socket Error')


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Websocket Disconnect")


def on_open(ws):
    print('Websocket Connect')
    # time.sleep(3)
    ws.send('{"message": "register", "register":"non_ip_data"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.5.146:9000/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
