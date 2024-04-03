
num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[32m", end=" ")
        tot += 1
    else:
        print("\033[m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[0mO numero {} foi divisivel {} vezes\033[m".format(num, tot))
if tot > 2:
    print("Este numero nao e primo, por ter {} divisoes".format(tot))
else:
    print("Esse numero e primo")
