#Faca um programa que tenha uma funcao chamada area(),
# que receba as dimensoes de um terreno retangular
# (largura e comprimento) e mostre a area do terreno.

def area(c, l):
    s = c * l
    print(f'A area do terreno ({c} x {l}) e de {s}m².')

print("Controle de terrenos")
area(float(input("Largura (m): ")), float(input("Comprimento (m): ")))
