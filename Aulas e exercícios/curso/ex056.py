#Deselvonva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A media de idades do grupo
#Nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

mulh = 0
velho = 0
media = 0
sexo = 0

print("=-="*15)
for n in range(1, 5):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: ")).lower().strip()
    print("=-="*15)
    if sexo == "feminino" or sexo == "f" and idade < 20:
        mulh += 1

    media += idade
###############################


print("Tem \033[0;32m{}\033[m mulheres menores que 20 anos".format(mulh))
print("O nome do homem meais velho e {}".format(velho))
print("Media das idades e igual a {:.2f}".format(media/4))
