#escreva um programaq que faca um computador "pensar" em um numero
#inteiro entre 0 e 5 e pe;a para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario venceu ou perdeu
import random

num = int(input("Pensei em um numero entre 0 e 5, tente adivinhar: "))
Nnum = int(random.uniform(0, 5))

if num == Nnum:
    print("\033[0;32mPARABENS VOCE ACERTOU\033[m!!!")
    print("Eu escolhi: \033[4m{}\033[m".format(Nnum))
else:
    print("\033[0;31mNao foi dessa vez...\033[m")
    print("Eu escolhi: \033[4m{}\033[m".format(Nnum))
