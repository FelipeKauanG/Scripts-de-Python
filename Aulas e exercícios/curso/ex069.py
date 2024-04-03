#Crie um programa que leia a idade  e o sexo de varias pessoas. A cada pessoa cadastrada
#o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre
#Quantas pessoas tem mais de 18 anos

#Quantos homens foram cadastrados.

#Quantas mulheres tem menos de 20 anos

print("-=-"*15)
print("CADASTRE PESSOAS")
print("-=-"*15)

cont = 0
esc = "g"
mulhe = 0
homem = 0
sexo = "1"
while esc != "n":

    cont += 1
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]")).lower().strip()[0]
    esc = str(input("Quer continuar ? [S/N]")).lower().strip()
    if sexo == "f" and idade < 20:
        mulhe += 1
    if sexo == "m":
        homem += 1
print(f"Ao todo foram {cont} pessoas")
print(f"Ao todo existe {mulhe} mulheres com menos de 20 anos")
print(f"Foram cadastrados {homem} homens")
