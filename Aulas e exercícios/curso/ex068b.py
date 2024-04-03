from random import randint
while True:
    vit = 0
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par OU impar [P/I]")).upper().strip()[0]
    print(f"Voce jogou {jogador} e o computador jogou {computador}. Total de {total}")
    print("DEU PAR" if total %2 == 0 else "Deu IMPAR")
    if tipo == "p":
        if total %2 == 0:
            print("Voce venceu!!!")
            vit += 1
        else:
            print("Voce perdeu")
            break

    elif tipo == "I":
        if total % 2 == 0:
            print("Voce venceu!!")
            vit += 1
        else:
            print("Voce perdeu!")
            break
    print("Vamos jogar novamente ?")
print(f"GAME OVER! voce venceu {vit} vezes")