s = 0
c = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for i in range(c, f+1, p):
    s += i
print("O resultado foi de \033[0;31m{}\033[m".format(s))
