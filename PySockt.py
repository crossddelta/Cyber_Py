#!/usr/bin/python
import socket
import sys

print("===================================================")
print("+                 P Y S O C K T                   +")
print("===================================================")

if len(sys.argv) <= 2:
    print("Informe um endereço IP e uma porta para verificar\nse a porta está disponível.")
    print("Modo de uso: python PySockt.py 192.168.0.1 80")

else:
    ip = sys.argv[1]
    port = int(sys.argv[2])

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    response = mysocket.connect_ex((ip, port))

    if response == 0:
        print(f"Sucesso! Porta {port} está aberta.")
    else:
        print(f"Falha! Porta {port} está fechada.")
