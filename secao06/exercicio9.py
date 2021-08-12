indice = float(input("Informe o índice de poluição: "))

if indice >= 0.3 and indice <0.4:
    print("As indústrias do primeiro grupo devem cessar suas atividades.")
elif indice >= 0.4 and indice <0.5:
    print("As indústrias do primeiro e segundo grupo devem cessar suas atividades.")
elif indice > 0.5:
    print("Todos os grupos devem cessar suas atividades.")
else:
    print("Índice de poluição em níveis aceitáveis.")