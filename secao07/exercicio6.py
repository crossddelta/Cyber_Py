num = int(input("Informe um número para ver a sua taboada: "))

for tab in range(1, 11):
    print("{0} x {1} = {2}".format(num, tab, (num * tab)))