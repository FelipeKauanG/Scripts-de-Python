nome = str(input("Qual e o seu nome: "))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Joao":
    print("Seu nome e bem popular no Brasil")
elif nome in "Ana Claudia Jessica Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome e bem normal")
print("Tenha um bom dia! {}".format(nome))

