#Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno
# individualmente.
lista = [], []  # alunos e notas
print("\033[0;31m▄\033[m"*40)
print("\033[0;36mBoletim escolar\033[m")
while True:
    while True:
        aluno = str(input("Nome do aluno: ")).strip().title()
        nota1 = [float(input("Nota \033[0;31m1\033[m: "))]
        nota2 = float(input("Nota \033[0;31m2\033[m: "))

        nota1.append(nota2)
        lista[1].append(nota1)

        per = str(input("Quer continuar ? \033[0;32m[S/N]\033[m")).lower().strip()[0]
        while per not in "sn":
            per = str(input("Quer continuar ? \033[4mAPENAS\033[m \033[0;31m[S/N]\033[m")).lower().strip()[0]
            if per == "n":
                break
        lista[0].append(aluno)
        if per == "n":
            break
    media = (lista[1][0][0] + lista[1][0][1])/2

    print("\033[0;31m█\033[m"*45)
    print("nº. Nome                                   \033[0;34mMedia\033[m")
    for i in range(0, len(lista[1])):
        print(f"{i+1} {lista[0][i]}".strip().title(), "."*(40-(len(lista[0][i]))), f"{(lista[1][i][0] + lista[1][i][1])/2:.2f}")
    print(f"_"*45)
    break
per2 = int(input("\n\nQuer ver a nota de qual aluno? \033[;33m[999]\033[m para parar!"))-1
print("\033[0;31m▄\033[m"*40)
while per != 998:
    print(f"\nAs notas de \033[0;36m{lista[0][per2]}\033[m sao \033[0;36m{lista[1][per2][0]}\033[m e \033[0;36m{lista[1][per2][1]}\033[m")
    per2 = int(input("Quer mais de qual aluno?"))-1
    if per2 == 998:
        break
print("\033[0;37mFim\033[m")
