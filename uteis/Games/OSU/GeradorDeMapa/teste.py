quantidade = 10

dicionarios = []

for i in range(1, quantidade+1):
    dicionario = {f"ID {i}: Item: {i}"}
    dicionarios.append(dicionario)

for dicionario in dicionarios:
    print(dicionario)
