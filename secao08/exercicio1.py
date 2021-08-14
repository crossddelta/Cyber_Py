#variaveis
vetor = []
pares = []

#entrada
for i in range(1, 6):
    vetor.append(i)
    if i % 2 == 0:
        pares.append(i)
for p in pares:
    print(p)