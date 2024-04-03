#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faca um programa que ajude ele, lendo o nome do escolhido
import random
a = str(input("Aluno \033[0;31mum\033[m: "))
b = str(input("Aluno \033[0;32mdois\033[m: "))
c = str(input("Aluno \033[0;33mtres\033[m: "))
d = str(input("aluno \033[0;34mquatro\033[m: "))

print("ALuno sorteado: \033[4;37m{}\033[m".format(random.choice([a, b, c, d])))

