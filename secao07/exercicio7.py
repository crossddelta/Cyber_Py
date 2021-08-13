quant = 0
idmouse = int(input("Informe o ID do mouse: "))
esfera = 0
limpeza = 0
cabo = 0
quebrado = 0

while idmouse != 0:
    quant = quant + 1
    print("Informe o problema do mouse: ")
    print("1 - Necessita esfera")
    print("2 - Necessita limpeza")
    print("3 - Necessita troca de cabo ou conector")
    print("4 - Quebrado ou inutilizado")
    problem = int(input())
    
    if problem == 1:
        esfera = esfera + 1
    elif problem == 2:
        limpeza = limpeza + 1
    elif problem == 3:
        cabo = cabo + 1
    elif problem == 4:
        quebrado = quebrado + 1
    idmouse = int(input("Informe o ID do mouse: "))
        
peresf = (esfera * 100) / quant
perlimp = (limpeza * 100) / quant
percab = (cabo * 100) / quant
perqueb = (quebrado * 100) / quant

print("Entre os {0} mouses testados há: ")
print("{0} com problemas na esfera. Isso representa {1}% dos mouses testados".format(esfera, peresf))
print("{0} com problemas na limpeza. Isso representa {1}% dos mouses testados".format(limpeza, perlimp))
print("{0} necessitam troca do cabo. Isso representa {1}% dos mouses testados".format(cabo, percab))
print("{0} estão quebrados ou inutilizados. Isso representa {1}% dos mouses testados".format(quebrado, perqueb))
    