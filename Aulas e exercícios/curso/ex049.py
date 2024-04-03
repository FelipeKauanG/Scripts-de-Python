#Refaca o desafio 009 mostrando a tabuada de um numero que o usuario escolher,
# so que agora utilizando o laco FOR
tabu = int(input("Tabuada de qual numero ?"))
amos = int(input("Quantas amostras quer ?"))

print("\033[0;36m-=-\033[m"*15)
for i in range(1, amos+1):
    res = i * tabu
    print("{} x {} = \033[0;32m{}\033[m".format(i, tabu, res))
print("\033[0;36m-=-\033[m"*15)