#!usr/bin/python
import urllib.request
from sys import argv

print("===================================================")
print("+                   U R L L I B                   +")
print("===================================================")

if(len(argv) <= 1):
	print("Informe um site para prosseguir!")
	print("Modo de uso: python URLlib.py 'http://www.google.com'")
else:
    site = urllib.request.urlopen(argv[1])
    server = site.info()

    print("O servidor web está rodando:")
    print("Imprimindo informações do Header...")
    print(server)
