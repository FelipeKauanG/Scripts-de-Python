# 1 - Escreva um programa que solicite ao usuário que digite uma palavra ou frase e, em seguida, exiba a contagem de cada palavra na entrada.

frase = str(input("Digite uma frase/palavra: ")).strip().title()
fraseSplit = frase.split()
for num, palavra in enumerate(fraseSplit):
    print(f"Número \033[31m{num+1}\033[m Palavra \033[36m{palavra}\033[m")