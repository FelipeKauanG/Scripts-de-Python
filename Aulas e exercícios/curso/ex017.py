#faca um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math

op = float(input("Cateto \033[0;31moposto\033[m: "))
ad = float(input("Cateto \033[0;34madjacente\033[m: "))

print("O comprimento da \033[0;33mhipotenusa\033[m mede {:.2f}:".format(math.hypot(op,ad)))
