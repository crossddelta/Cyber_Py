#variáveis
excesso = 0
multa = 4 * excesso

#entrada
peso = float(input("Informe o valor do peso da pesca: "))

#processamento
if peso > 50:
    excesso = (peso - 50)
    multa = 4 * excesso
    
#saída
print("O peso da pesca foi de {0}kg".format(peso))
print("Portanto, o excedente foi de {0}kg, gerando uma multa de R${1:.2f}".format(excesso, multa))
