#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n1 = int(input("Escreva um valor em metros: "))

print("O valor em Centímetros é \033[0;31m{}\033[m, "
      "\nO valor em Milímetros é \033[0;32m{}\033[m".format(n1*100, n1*1000))
