#!/usr/bin/python
import phonenumbers
from phonenumbers import geocoder, carrier

print("===============================================================")
print("+              S I M P L E   P H O N E   R E C O N            +")
print("===============================================================")
print("Informe o celular com código do país e ddd.\nExemplo: +5511912345678\n")
# Recebe o número com código do país e ddd
numPhone = phonenumbers.parse(input("Informe um número de celular para identificar sua operadora e região: "))
# Identifica operadora
operadora = carrier.name_for_number(numPhone, 'pt-br')
# Identifica região
regiao = geocoder.description_for_number(numPhone, 'pt-br')

print("\n=========================================")
print(f"Informações sobre o número:")
print(f"+ Operadora: {operadora}")
print(f"+ Região: {regiao}")
print("=========================================")
