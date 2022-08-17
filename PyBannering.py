#!/usr/bin/python
import socket
from time import sleep

print("===================================================")
print("+               B A N N E R I N G                 +")
print("===================================================")

ip = input("Informe o endereço ip do host alvo: ")
port = int(input("\nInforme a porta que deseja verificar: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sleep(1)

sock.connect((ip, port))

banner = sock.recv(1024)

print(banner)
