vetor = []
soma = 0

for n in range(0, 20):
    num = int(input("Informe um valor para a posição {0}/20 do vetor: ".format(n+1)))
    vetor.append(num)
    #soma = soma + num

print("A soma de todos os elementos informados é: {0}".format(sum(vetor)))