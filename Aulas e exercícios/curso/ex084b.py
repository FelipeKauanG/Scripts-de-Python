#Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final moste:
#A) Quantos pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

dados = []
cont = 0
pesada = []
leve = []
while True:


    nome = str(input("Nome: "))
    peso = int(input("Peso: "))

    dados.append(nome) #dados[0]
    dados.append(peso) #dados[1]

    if cont == 0:
        pesada.append(dados[:])
        leve.append(dados[:])

    if dados[1] > pesada[0][1]:
        pesada.clear()
        pesada.append(dados[:])

    if dados[1] < leve[0][1]:
        leve.clear()
        leve.append(dados[:])

    cont += 1
    per = str(input("Quer continuar ? ")).lower().strip()[0]
    dados.clear()

    while per not in "sn":
        per = str(input("Quer continuar ? ")).lower().strip()[0]

    if per == "n":
        break

if cont == 1:
    print(f"Apenas uma pessoa digita, portanto ela e \033[0;35m"
          f"{leve[0][0].title().strip()}\033[m com \033[0;36m{leve[0][1]}\033[mkg")
else:
    print(f"Foram cadastradas {cont} pessoas")
    print(f"A pessoa mais leve e \033[0;35m"
          f"{leve[0][0].title().strip()}\033[m com \033[0;36m{leve[0][1]}\033[mkg")
    print(f"A pessoa mais pesada e \033[0;35m{pesada[0][0].title().strip()}"
          f"\033[m com  \033[0;36m{pesada[0][1]}\033[mkg")
