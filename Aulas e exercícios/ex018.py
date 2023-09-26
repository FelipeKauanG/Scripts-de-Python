# faca um programa que leia um angulo qualquer, e mostre na tela o valor do seno cosseno e tangente.
import math
from math import sin, cos, tan

ang = float(input("Angulo :"))
print("\033[0;32mSeno\033[m: {:.3f}\n"
      "\033[0;31mCosseno\033[m {:.3f}\n"
      "\033[0;36mTangente\033[m: {:.3f}".format(sin(math.radians(ang)), cos(math.radians(ang)), tan(math.radians(ang))))

# converter em radianos
