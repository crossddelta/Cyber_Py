maior = 0
menor = 99999
soma = 0

for i in range(1, 11):
    num = int(input("Informe o valor {0}/10: ".format(i)))
    if num > 0: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma = soma + num

media = soma / 10
print("A média dos valores inseridos é: {0}".format(media))
print("O maior valor inserido foi: {0}".format(maior))
print("O menor valor inserido foi: {0}".format(menor))