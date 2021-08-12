#entrada
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
n3 = int(input("Informe o terceiro valor: "))
n4 = int(input("Informe o quarto valor: "))

#processamento
q1 = n1 * n1
q2 = n2 * n2
q3 = n3 * n3
q4 = n4 * n4

#saida
if q3 > 1000:
    print("O quadrado do terceiro número ({0}) é: {1}".format(n3, q3))
else:
    print(q1)
    print(q2)
    print(q3)
    print(q4)