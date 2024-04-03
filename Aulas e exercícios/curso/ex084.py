#Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final moste:
#A) Quantos pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

cont = 0
pessoas = [[], [], [], []] #pessoa mais pesada, pessoa mais leve, maior, menor
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))

    if cont == 0:
        for i in range(0, 2):
            pessoas[i].append(nome)
        for i in range(2, 4):
            pessoas[i].append(peso)

    if cont >= 1:
        if peso > pessoas[2][0] and peso > pessoas[3][0]:
            pessoas[0].clear()
            pessoas[2].clear()
            pessoas[0].append(nome)
            pessoas[2].append(peso)

        if peso < pessoas[3][0]:
            pessoas[1].clear()
            pessoas[3].clear()
            pessoas[1].append(nome)
            pessoas[3].append(peso)

    cont += 1
    per = str(input("Quer continuar ? [S/N]")).lower().strip()[0]
    if per not in "sn":
        per = str(input("Quer continuar ? [S/N]")).lower().strip()[0]
    if per == "n":
        break

print(f"Foram cadastradas {cont} Pessoas")
if cont == 1:
    print(f"Uma pessoa registrada: \033[0;36m{pessoas[0][0]}\033[m com {pessoas[2][0]}Kg")
else:
    print(f"A pessoa mais pesada e \033[0;36m{pessoas[0][0]}\033[m com {pessoas[2][0]}Kg")
    print(f"A pessoa mais leve e \033[0;36m{pessoas[1][0]}\033[m com {pessoas[3][0]}Kg")
