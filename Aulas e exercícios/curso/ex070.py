#Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar
#se o usuario quer continuar.
#No final , mostre:

#Qual e o total gasto na compra

#Quantos produtos custam mais de R$1.000

#Qual e o nome do produto mais barato

print("-=-"*15)
print("LOJA SUPER BARATAO")
print("-=-"*15)

menor = 9999999999999999999
total = 0
esc = "1"
contmil = 0
nomepreco = ""
while esc != "n":
    nome = str(input("Nome do produto: "))
    preco = float(input("Preco: "))
    esc = str(input("Quer continuar ? [S/N]")).lower().strip()
    if preco < menor:
        menor = preco
        nomepreco = nome
    if preco > 1000:
        contmil += 1
    total += preco

print(f"O produto mais barato e \033[0;35m{nomepreco}\033[m que custa \033[0;32mR${menor}\033[m")
print(f"Foram {contmil} produto(s) maior do que 1000 reais")
print(f"O total deu \033[0;32mR${total}\033[m")
