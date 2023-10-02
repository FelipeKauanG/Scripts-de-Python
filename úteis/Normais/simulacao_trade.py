from random import randint
from time import sleep

per = int(input("Quanto voce quer investir ?R$"))
while True:
    total = per
    aleatorio = randint(-10, 10)/100
    total += aleatorio
    if total < per:
        print(f"\033[0;31mR${total:.2f}\033[m   ", end="")
    elif total > per:
        print(f"\033[0;32mR${total:.2f}\033[m   ", end="")
    sleep(1)
