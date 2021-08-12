#variaveis
maior = 0

#entrada
num = int(input("Informe um número: "))

#processamento
while num != 0:
    if num > maior:
        maior = num
    num = int(input("Informe um número: "))

#saída
print("O maior número informado é: {0}".format(maior))