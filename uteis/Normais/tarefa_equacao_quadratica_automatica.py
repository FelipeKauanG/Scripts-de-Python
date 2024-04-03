from random import randint, choice
from time import sleep
from math import sqrt
print("\033[0;35mTarefa de raiz quadrada automatica!\033[m")
a = randint(1, 10)
b = randint(0, 10)
c = randint(0, 10)

delta = (b**2) - 4*a*c
raiz = delta**0.5
esc = " "
per = " "
print(f"\n\033[0;36m{a}x² + {b}x + {c} = 0 : \033[m")


