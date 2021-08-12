num = int(input("Informe um valor: "))

if num % 2 == 0:
    print("O número {0} é par".format(num))
    if num > 0:
        print("{0} também é positivo".format(num))
    else:
        print("{0} também é negativo".format(num))
else:
    print("O número {0} é ímpar".format(num))
    if num > 0:
        print("{0} também é positivo".format(num))
    else:
        print("{0} também é negativo".format(num))