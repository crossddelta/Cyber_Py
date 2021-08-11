#variavel
excesso = 0

#entrada
horas_trab = int(input("Informe a quantidade de horas trabalhadas: "))

#processamento
salario = 10 * horas_trab

if horas_trab > 50:
    excesso = horas_trab - 50
    salario += (20 * excesso)

#saida
print("O salário desse mês será de R${0:.2f}, o número de horas extras foi: {1}".format(salario, excesso))