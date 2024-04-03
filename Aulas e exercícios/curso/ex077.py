#Crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
#Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.

palavras = "Batalha", "Curso", "Video", "Python", "Tijela", "Palavra", "Vogal", "Estrela", "Lousa", "Hipopotamo",\
           "Jabuti", "Papel", "Buraco negro", "Mercedes", "Minecraft"


for p in palavras:
    print(f"\nNa palavra \033[0;36m{p.upper()}\033[m, temos as vogais ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"\033[0;36m{letra}\033[m", end="")
