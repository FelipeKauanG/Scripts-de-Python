# escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor e maior
#o segundo e maior
#nao existe valor maior, os dois sao iguais

n1 = float(input("\033[0;34mDigite um valor: \033[m"))
n2 = float(input("\033[0;36mDigite Mais um valor: \033[m"))

if n1 > n2:
    print("O \033[0;33mprimeiro\033[m valor e \033[0;32mmaior\033[m.")
elif n1 < n2:
    print("O \033[0;33msegundo\033[m valor e \033[0;32mmaior\033[m.")
elif n1 == n2:
    print("Os \033[0;32mValores\033[m sao exatamente \033[0;32miguais\033[m.")
