vetor = []

for n in range (0, 10):
    num = int(input("Informe o valor {0}/10 para o vetor: ".format(n+1)))
    vetor.append(num)
    
vetor.reverse()
for n in vetor:
    print(n)