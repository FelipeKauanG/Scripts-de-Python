#Desenvolva um programa que leia o primeiro termo e a raxao de uma PA. No final,
# mostre os 10 primeiros termos dessa prograssao

n = int(input("Primeiro termo: "))
r = int(input("Razao: "))

print("\033[0;36m{}\033[m".format(n), end=" ")

for i in range(1, 10):

    print(n + r * i, end=" ")
