# rafaca o desafio dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado
#equilatero: todos os lados iguais
#isosceles: dois lados iguais
#escaleno: todos os lados diferentes

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

print("\033[0;31m===\033[m"*15)
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print("\033[0;36mPodemos formar um triangulo\033[m ")
    if r1 == r2 and r2 == r3:
        print("Temos um \033[0;35mtriangulo equilatero\033[m")
    elif r1 != r2 and r2 != r3:
        print("Temos um triangulo \033[0;32mescaleno\033[m")
    else:
        print("Temos um trianglo \033[0;31misosceles\033[m")

else:
    print("\033[0;31mNao podemos formar um triangulo\033[m")
