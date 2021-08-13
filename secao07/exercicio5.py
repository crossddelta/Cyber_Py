nome = input("Informe o seu nome: ")
senha = input("Informe a sua senha: ")

while nome == senha:
    print("Nome e senha devem ser diferentes.")
    nome = input("Informe o seu nome: ")
    senha = input("Informe a sua senha: ")