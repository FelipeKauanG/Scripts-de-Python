# crie um programa que leia duas notas de um aluno e calcule sua media,
# mostrando uma mensagem no final, de acordo com a media atingida.
# media abaixo de 5.0 = reprovado
# media entre 5 e 6.9 = recuperacao
# media 7 ou superior = aprovado

bim1 = float(input("Nota do 1 bimestre: "))
bim2 = float(input("Nota do 2 bimestre: "))
media = (bim1 + bim2) / 2

if media >= 7:
    print("\033[0;32mAprovado\033[m")
elif media < 5:
    print("\033[0;31mReprovado\033[m")
else:
    print("\033[0;33mRecuperacao\033[m")
