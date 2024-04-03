import math
#Desenvolva um prigrama que leia o comprimento de 3 retas e diga
# ao usuario se elas podem ou nao formar um triangulo

import math

sen = float(input("reta 1"))
cos = float(input("reta 2"))
tan = float(input("reta 3"))

if sen**2 + cos**2 == tan**2:
    print("Podemos formar um triangulo retangulo")
else:
    print("Nao podemos formar um triangulo retangulo")
 