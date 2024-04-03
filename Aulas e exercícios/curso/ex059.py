#crie um programa que leia dois valores e mostre um menu na tela:

#1 soma
#2 multiplicar
#3 maior
#4 novos numeros
#5 sair do programa

#seu programa devera realizar a operacao solicitada em cada caso.
print("\033[0;35mCalculadora\033[m")
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite mais um valor: "))
esc = int(input("""                       \033[0;34m[1] SOMAR\033[m 
                       \033[0;31m[2] MULTIPLICAR\033[m
                       \033[0;35m[3] MAIOR\033[m                         
                       \033[0;32m[4] NOVOS VALORES\033[m 
                       \033[0;37m[5] SAIR DO PROGRAMA\033[m """))

if esc == 1:
        print("A soma entre \033[0;33m{}\033[m e \033[0;31m{}\033[m vale \033[0;36m{}\033[m".format(num1, num2, num1 + num2))

if esc == 2:
        print("\033[0;33m{}\033[m multiplicado com \033[0;31m{}\033[m vale \033[0;36m{}\033[m".format(num1, num2, num1 * num2))

if esc == 3:
        if num1 > num2:
            print("\033[0;32m{}\033[m e o maior". format(num1))
        elif num1 < num2:
            print("\033[0;32m{}\033[m e o maior".format(num2))
        else:
            print("\033[0;36mOs valores sao iguais!\033[m")

if esc == 4:
        num1 = int(input("Digite um valor"))
        num2 = int(input("Digite mais um valor:"))
print("Voce saiu do programa!")
