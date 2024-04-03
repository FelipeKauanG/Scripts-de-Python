#Escreva um programa que leia um numero n inteiro qualquer e mostre
#na tela os n primeiros elementos de uma sequencia de Fibonacci,
#ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

print("-=-"*15)
print("Sequencia de Fibonacci")

num = int(input("Quantos termos quer ?"))

t1 = 0
t2 = 1

termos = 3
print(t1)
print(t2)
while termos <= num:
    termos += 1
    t3 = t1 + t2
    print("{}".format(t3))
    t1 = t2
    t2 = t3
print("\n\033[0;31mFim\033[m")
