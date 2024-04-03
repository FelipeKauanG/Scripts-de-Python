#faca um programa que calcula a distancia maxima e a altura maxima

import math

Vo = float(input("Velocidade do objeto (M/S): "))
ang = float(input("Angulo do objeto (º): "))

Vox = (Vo*(math.cos(math.radians(ang))))   #velocidade horizontal
Voy = (Vo*(math.sin(math.radians(ang))))   #velocidade vertical

tempo_subida = (Voy / 9.8)   #calcula o tempo de subida


alc = (Vox*tempo_subida*2)   #calcula o alcance maximo
alt = (Voy ** 2) / (2 * 9.81)   # calcula a altura maxima

print("\033[0;32mAlcance maximo:\033[m {:.2f}m\n"
     "\033[0;36mAltura maxima:\033[m {:.2f}m".format(alc, alt))

print("\033[0;31mTempo de subida e descida\033[m {:.2f}S".format(tempo_subida*2))
