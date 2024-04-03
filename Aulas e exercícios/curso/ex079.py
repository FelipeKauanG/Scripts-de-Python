#Crie um programa onde o usuario possa digitar varios valores numericos e cadastre- os em uma lista
#Caso o numero ja existe la dentro, ele nao sera adicionado.
#No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Nao vou adicionar...")
    per = str(input("Quer continuar ? [S/N]")).strip().lower()
    while per not in "sn":
        per = str(input("[S/N]")).strip().lower()
    if per not in "s":
        break
lista.sort()
print(f"Os valores cadastrados na lista foram {sorted(lista)}")
