import socket
import time
import json
HOST = '127.0.0.1'
PORT = 5004

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = 'Hello, world!'
        ja=json.dumps(message).encode()
        s.sendall(ja)
        time.sleep(3)
    # print("connected")
    # message = 'Hello, world!'
    # #
    #
    # ja=json.dumps(message).encode()
    # s.sendall(ja)
    # time.sleep(3)
