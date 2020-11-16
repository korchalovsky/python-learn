import socket
import sys

port = 7001
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    serverSocket.bind(('', port))
except OSError:
    print('Порт, на котором вы пытаетесь запустить сервер, занят')
    sys.exit()

print("waiting on port:", port)

while 1:
    data, addr = serverSocket.recvfrom(1024)
    print(data.decode())
    message = "Hello, I'm UDP server".encode()
    serverSocket.sendto(message, addr)
