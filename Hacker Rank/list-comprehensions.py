import numpy as np

x = int(input("Insira o valor de X: "))
y = int(input("Insira o valor de Y: "))
z = int(input("Insira o valor de Z: "))
coords = [x, y, z]
permutations = []



for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            coord = i,j,k
            permutations.append(coord)



print(permutations)