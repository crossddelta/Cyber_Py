#!/usr/bin/python
import requests
from sys import argv

print("===================================================")
print("+                R E Q U E S T S                  +")
print("===================================================")

if(len(argv) <= 1):
	print("Informe um site para prosseguir!")
	print("Modo de uso: python Requests.py 'http://www.google.com'")
else:
	site = requests.get(argv[1])
	status = site.status_code

	if(status == 200):
		print("Página disponivel!")
		print("Imprimindo informações do Header...")
		print(site.headers)
	else:
		print("Página indisponível ou inexistente")
