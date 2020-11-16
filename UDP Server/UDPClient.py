import socket  # for sockets
import sys  # for exit

# create dgram udp socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 7001

while 1:

    message = input('Enter message to send : ')
    try:
        # Set the whole string
        clientSocket.sendto(message.encode(), (host, port))
        # receive data from client (data, addr)
        data = clientSocket.recvfrom(1024)
        reply = data[0].decode()
        addr = data[1]
        print('Server reply : ' + reply)

    except socket.error as msg:
        print("Socket Error:", msg)
        sys.exit()
