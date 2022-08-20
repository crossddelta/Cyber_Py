#!/usr/bin/python
import socket

print("===================================================")
print("+              P Y S E R V E R S I M              +")
print("===================================================")
print("Aguardando conexão...")
port = 12397
sock = socket.socket()
sock.bind(('', port))

sock.listen(5)
while True:
    c, addr = sock.accept()
    print("Sucesso!")
    print(f"Conexão recebido de: {addr}")
    confirm = (f'Obrigado por se conectar!')
    c.send(confirm.encode())
    c.close()
