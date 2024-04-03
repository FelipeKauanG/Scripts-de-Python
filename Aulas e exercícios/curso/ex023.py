#faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

num = int(input("Digite um numero de 0 ate 9999: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("\033[0;34mUnidade:\033[m {} \n"
      "\033[0;31mDezena:\033[m {}\n"
      "\033[0;34mCentena:\033[m {}\n"
      "\033[0;31mMilhar:\033[m {}".format(u, d, c, m))
