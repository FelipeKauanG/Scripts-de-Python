# Faca um programa que tenha um funcao chamada contador() que receba tres paramentros:
# inicio, fim e passo e realize a contagem:
# seu programa tem que realizar tres contagens atrasves da funcao criada:
# De 1 ate 10, de 1 em 1
# De 10 ate 0, de 2 em 2
# Uma contagem personalizada.

from time import sleep


def contador(i, f, p):

    if i < f and p < 0:
        p *= -1
    elif p == 0 and i > f:
        p = -1
    elif p == 0 and i < f:
        p = 1


    print("=" * 30)
    sleep(1)
    if i > f:  # de tras pra frente
        a = -1
    elif i < f:  # de frente pra tras
        a = 1
    print(f"Contagem de {i} ate {f} de {p * a} em {p * a}")
    for cont in range(i, f + a, p):
        print(f"{cont}", end=" ")
        sleep(0.2)
    print(f"Fim!")
    print()


contador(1, 10, 1)
contador(10, 0, -2)
print("Agora e a sua vez de personalizar a contagem!")
contador(i=int(input("\n\033[0;36mInicio: \033[m")), f=int(input("\033[0;36mFim: \033[m")), p=int(input("\033[0;36mPasso: \033[m")))
