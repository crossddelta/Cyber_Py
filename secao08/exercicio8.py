vetor = []

codigo = int(input("Informe o codigo: "))

if codigo != 0:
    for i in range(1, 6):
	    num = int(input("Informe o {0}º valor: ".format(i)))
	    vetor.append(num)
    if codigo == 1:
	    for i in vetor:
		    print(i)
    elif codigo == 2:
	    vetor.reverse()
	    for i in vetor:
		    print(i)
    else:
        print("Codigo invalido.")