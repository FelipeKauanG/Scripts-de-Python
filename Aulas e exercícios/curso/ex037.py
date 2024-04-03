#Escreva um programa que leia um numero qualquer e peca para o usuario escolher qual sera a base de conversao:
#1 para binario
#2 para octal
# para hexadecimal

num = int(input("Digite um numero: "))

print("\033[0;34m-\033[m=\033[0;31m-\033[m"*15)

print("\033[0;36m1 para Binario\033[m\n"
      "\033[0;3m2 para Octal\033[m\n"
      "\033[0;32m3 para Hexadecimal\033[m")

esc = int(input("Escolha um numero de \033[0;32m1\033[m a \033[0;33m3\033[m: "))


if esc > 3:
    print("\033[0;31mEscolha invalida!\033[m")

elif esc == 1:
    print("\033[0;36mValor Binario: {}\033[m".format(bin(num)))

elif esc == 2:
    print("\033[0;mValor em Octal: \033[m{}".format(oct(num)))

elif esc == 3:
    print("\033[0;32mValor em Hexadecimal: \033[m{}".format(hex(num)))
