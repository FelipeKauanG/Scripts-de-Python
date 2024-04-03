#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte
#ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar
# quantas cedulas de cada valor serao entregues.

#obs: Considere que o caixa possui cedulas de R50, R$20, R$10 e R$1.

print("-=-"*15)
print("\033[0;34mBANCO CEV\033[m")
print("-=-"*15)
num = int(input("Valor a ser sacado: "))

cinq = num // 50
vint = num % 50 // 20
dez = num % 50 % 20 // 10
um = num % 50 % 20 % 10 // 1

print(f"""          Total de {cinq} cedulas de \033[0;31mR$50,00\033[m
          Total de {vint} cedulas de \033[0;33mR$20,00\033[m
          Total de {dez} cedulas de \033[0;35mR$10,10\033[m
          Total de {um} cedeulas de \033[0;32mR$1,00\033[m""")
print("\nVolte sempre ao \033[0;34mBANCO CEV\033[m! tenha um bom dia!")
