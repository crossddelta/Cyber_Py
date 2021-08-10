valor_hora = float(input("Informe qual o valor de cada hora trabalhada: "))
horas_trab = int(input("Informe quantas horas trabalhou no mês: "))

salario = valor_hora * horas_trab

print("Seu salário será de: R${0:.2f}".format(salario))
