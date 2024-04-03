#Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido
#quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no
#final de jogo

from random import randint

print("-=-"*15)
print("VAMOS JOGAR PAR OU IMPAR")
print("-=-"*15)

comp = randint(0, 10)
esc = -1
cont = 0
while esc != comp:
    num = int(input("Diga um valor: "))
    esc = str(input("Par ou Impar ? [P/I]")).lower().strip()
    print("-=-"*15)

    if esc in "Pp":
        if (num + comp) % 2 == 0:
            print(f"Voce jogou {num} e escolheu PAR, o computador jogou {comp}. Total de {num + comp} deu PAR")
            print("Voce \033[0;32mvenceu!!\033[m")
            cont += 1
            print("-=-" * 15)
        if (num + comp) % 2 != 0:
            print(f"Voce jogou {num} e escolheu PAR, o computador jogou {comp}. Total de {num + comp} deu IMPAR")
            print("Voce \033[0;31mPERDEU!!\033[m")
            break
        if esc not in "PpIi":
            break

    if esc in "Ii":
        if (num + comp) % 2 == 0:
            print(f"Voce jogou {num} e escolheu IMPAR, o computador jogou {comp}. Total de {num + comp} deu PAR")
            print("Voce \033[0;31mPERDEU!!\033[m")
            print("-=-" * 15)
            break
        if (num + comp) % 2 != 0:
            print(f"Voce jogou {num} e escolheu IMPAR, o computador jogou {comp}. Total de {num + comp} deu IMPAR")
            print("Voce \033[0;32mVENCEU!!!\033[m")
            cont += 1
            print("-=-"*15)
if cont == 1:
    print("Voce ganhou uma unica vez , mais sorte da proxima vez!")
elif cont > 1:
    print(f"Voce ganhou \033[0;35m{cont}\033[m vezes consecutivas!!!")
elif cont > 10:
    print("Voce realmente sabe jogar, voce ganhou {} vezes consecutivas!!!")
    print("\033[0;31mParabens!!!\033[m")
if cont == 0:
    print("Tenta ganhar dele denovo!!!")