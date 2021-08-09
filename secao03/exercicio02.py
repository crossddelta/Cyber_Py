#Entrada
quant_min = int(input("Informe a quantidade mínima: "))
quant_max = int(input("Informe a quantidade máxima: "))

#Processamento
estoque_med = (quant_min + quant_max)/ 2

#Saída
print("O estoque médio é de {0}".format(estoque_med))