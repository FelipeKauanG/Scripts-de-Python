#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa
# em um dicionario e todos os dicionarios em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas
# B) A media de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todos as pessoas com idade acima da media
print("     \033[0;35;21mCadastro de pessoas\033[m")
tema = int(input("""Tema \033[0;31mE\033[m\033[0;34mU\033[m\033[0;31mA\033[m[0]
Tema \033[0;34mB\033[m\033[0;33mR\033[m\033[0;32mL\033[m[1]
Sem tema [-1]"""))
while tema < -1 or tema > 1:
    tema = int(input("""Escolha 0 para tema EUA , 1 para tema BRL ou -1 para sem tema!"""))

if tema == 0:
    print("Voce escolheu o tema \033[0;31mE\033[m\033[0;34mU\033[m\033[0;31mA\033[m")
    tema = (31, 34, 31, 34, 31, 34)# Brasil
elif tema == 1:
    print("Voce escolheu o tema \033[0;34mB\033[m\033[0;33mR\033[m\033[0;32mL\033[m")
    tema = (32, 33, 34, 33, 32, 34)# EUA
if tema == -1:
    print("Voce escolheu um tema personalizado predefinido")
    tema = (36, 33, 35, 95, 32, 32)# sem tema
print("\n")


dados = dict()
mulheres = list()
lista = list()
media = cont = 0
while True:
    dados["Nome"] = str(input("Nome :")).strip().title()
    dados["Idade"] = int(input("Idade: "))
    media += dados["Idade"]
    dados["Sexo"] = str(input("Sexo:  [M/F]")).strip().lower()[0]

    while dados["Sexo"] not in "mf":
        dados["Sexo"] = str(input("Erro: Digite [M/F]")).strip().lower()[0]
    if dados["Sexo"] == "f":
        mulheres.append(dados["Nome"])
    cont += 1
    lista.append(dados.copy())
    per = str(input("Quer continuar [S/N]?")).strip().lower()[0]
    while per not in "sn":
        per = str(input("Erro, digite [S/N]")).strip().lower()[0]
    if per == "n":
        break
print("=-="*30)

print(f"\nForam cadastradas \033[0;{tema[0]}m{cont} pessoas\033[m")
print(f"A media de idade do grupo e de \033[0;21;{tema[1]}m{media/cont:.1f}\033[m anos")



print(f"Lista com todas as \033[0;{tema[2]}mmulheres\033[m: ")
if len(mulheres) == 0:
    print("Nao ha nenhuma mulher")
else:
    for mul in mulheres:
        print(f"     \033[0;{tema[3]}m{mul}\033[m")



if cont > 1:
    print("Pessoas com idade acima da media")
for pess in lista:
    if pess["Idade"] > media/cont:
        print(f"     \033[0;21;{tema[4]}m{pess['Nome']}\033[m", end="")
        print(f" com \033[0;{tema[5]}m{pess['Idade']}\033[m anos")
print("\n\033[0;21mFIM\033[m")
