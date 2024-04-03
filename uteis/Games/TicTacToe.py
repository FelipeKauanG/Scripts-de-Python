
def game():
    print(f"\033[31mBEM VINDOS AO JOGO DA VELHA\033[m")

    simbol = str(input(f"Qual você quer escolher \033[31;1m○\033[m(1) ou\033[34m x \033[m(2)?")).strip().split(" ")
    #simbol = str(input(f"Por favor escolha apenas números inteiros! \033[31;1m○\033[m(1) ou\033[34m x \033[m(2)?")).strip().split

    print(simbol)


game()
