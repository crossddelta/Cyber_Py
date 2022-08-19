#!/usr/bin/python

import socket

print("===================================================")
print("+              P Y C L I E N T S I M              +")
print("===================================================")

sock = socket.socket()
host = socket.gethostname()
port = 12397

sock.connect((host, port))
print(sock.recv(1024))

sock.close()
