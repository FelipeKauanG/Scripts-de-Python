from random import randint, choice
from time import sleep
from math import sqrt
print("\033[0;35mTarefa de raiz quadrada manual!\033[m")
a = randint(1, 10)
b = randint(0, 10)
c = randint(0, 10)

delta = (b**2)-4*a*c
raiz = delta**0.5
esc = " "
per = " "
print(f"\n\033[0;36m{a}x² + {b}x + {c} = 0 : \033[m")
while True:
    if per not in "s":
        per = str(input("Mostrar o resultado, digite [S]")).lower().strip()[0]
    elif per in "s":
        print("Mostrando o valor de Delta", end="")
        for seg in range(0, 3):
            sleep(0.5)
            print(".", end="")
        break
if delta > 0:
    if sqrt(delta) % 1 == 0:
        print(f"O valor de Delta e {delta}")
        print(f"E sua raiz e igual a {sqrt(delta)}")
        print(f"\nX1 = {(-b + raiz )/(2*a):.3f}"
              f"\nX2 = {(-b - raiz )/(2*a):.3f}")
    else:
        print(f"\nO valor de Delta e {delta}")
        print("Nao temos raizes exatas!")
else:
    print("\nRaiz de Delta menor do que 0")
