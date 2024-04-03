#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar
#Quando o usuario digitar 999, que e a condicao de parada.
#No final, mostre quantos numeros foram digitados qual foi a soma entre eles(desconsiderando o
#flag).

cont = 0
n = int(input("Digite um valor: "))
cont += n
contnum = 0
num = 0
while num != 999:
    num = int(input("Digite outro valor: "))
    contnum +=1
    if num == 999:
        break
    cont += num
print(f"A soma dos {contnum} numeros foi \033[0;34m{cont}!\033[m")
