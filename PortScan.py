#!/usr/bin/python
import socket
from sys import argv

print("===================================================")
print("+                P O R T S C A N                  +")
print("===================================================")

if len(argv) <= 1:
    print("Informe um endereço IP para verificar todas as\nportas disponíveis no host.")
    print("Modo de uso: python PortScan.py 192.168.0.1")

else:
    ip = argv[1]

    print("Escaneando...")

    for port in range(1,65536):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(3)

        response = mysocket.connect_ex((ip, port))

        if response == 0:
            print(f"Sucesso! Porta {port} está aberta.")
            mysocket.close()
        else:
            mysocket.close()
