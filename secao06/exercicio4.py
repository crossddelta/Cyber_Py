#entrada
altura = float(input("Informe a sua altura: "))
sexo = input("Informe o seu sexo (m/f): ")
#peso_ideal = 0

#converte sexo para maiúsculo para checagem
if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else: 
    print("Sexo não reconhecido.")
    
print("Seu peso ideal é: {0:.1f}".format(peso_ideal))
    