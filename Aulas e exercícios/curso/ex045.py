#crie um programa que faca o computador jogar jokenpo com voce.

from random import randint
from time import sleep

jogada = int(input("\033[0;34mJokempo\033[m\n"
                   " 1 Para Pedra: \n"
                   " 2 para Papel: \n"
                   " 3 Para Tesoura: "))
escolha = randint(1, 3)

if jogada == 1 and escolha == 2:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("Papel cobre pedra!, voce \033[0;31mperdeu!\033[m que pena...")
elif jogada == 1 and escolha == 3:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("Pedra quebra tesoura!, \033[0;32mvoce venceu\033[m")
elif jogada == 1:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("\033[0;33mEmpate!!!\033[m\n"
          "Pedra com pedra...")



if jogada == 2 and escolha == 1:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("Papel cobre pedra!, voce \033[0;32mvenceu!!!\033[m")
elif jogada == 2:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("\033[0;33mEmpate!!!\033[m\n"
          "Papel com papel...")
elif jogada == 2 and escolha == 3:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("Tesoura corta papel!!!, voce \033[0;31mperdeu!\033[m, que pena...")



if jogada == 3 and escolha == 1:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("Pedra quebra tesoura!!!, voce \033[0;31mperdeu\033[m que pena...")
elif jogada == 3 and escolha == 2:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("Tesoura corta papel!!!, Voce \033[0;321"
          "\033[0;32Voce venceu!!!\033[m")
elif jogada == 3:

    sleep(0.2)
    print("JOKEMPO")
    sleep(1.3)
    print("\033[0;33mEmpate!!!\033[m\n"
          "Tesoura com tesoura...")
elif jogada > 3 or jogada < 1:

    print("Ei!, esta tentando sair do jogo?")
