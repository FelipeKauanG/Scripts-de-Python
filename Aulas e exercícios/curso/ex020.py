# o mesmo professor do desafio anterior que
# r sortear a ordem de apresentacao de trabalhos dos alunos. faca um programa que leia o nome dos quatro
# alunos e mostre a ordem sorteada
import random
a = str(input("\033[0;31mAluno um\033[m: "))
b = str(input("\033[0;32mAluno dois\033[m: "))
c = str(input("\033[0;33mAluno tres\033[m: "))
d = str(input("\033[0;34mAluno quatro\033[m: "))

print("A ordem sao \033[4m{}\033[m".format(random.sample([a,b,c,d], k=4)))
