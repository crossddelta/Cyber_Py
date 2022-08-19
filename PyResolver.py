import socket
from sys import argv

print("===================================================")
print("+              P Y R E S O L V E R                +")
print("===================================================")

if len(argv) <= 1:
    print("Informe um endereço para prosseguir!")
    print("Modo de uso: ./PyResolver 'www.google.com'")
else:
    host = argv[1]

    print(f"Host: {host} | IP: {socket.gethostbyname(host)}")
