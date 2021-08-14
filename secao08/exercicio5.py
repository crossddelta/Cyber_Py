vetor = []
maior50 = False

for n in range(0, 10):
    num = int(input("Informe o {0}º valor do vetor: ". format(n+1)))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print("Número {0} : posição {1}".format(n, vetor.index(n)))
        maior50 = True
if maior50 == False:
    print("Nenhum número informado é superior a 50.")