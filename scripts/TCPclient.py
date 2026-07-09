#!/usr/bin/env python3

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host
host = socket.gethostname()

port = 444

clientsocket.connect(('ip',port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
