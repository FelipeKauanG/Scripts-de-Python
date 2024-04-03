#Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou IMPAR

Num = int(input("Digite um numero qualquer"))
if Num % 2 == 0:
    print("{} E um numero \033[0;36mPAR\033[m".format(Num))
else:
    print("{} E um numero \033[0;31mIMPAR\033[m".format(Num))
