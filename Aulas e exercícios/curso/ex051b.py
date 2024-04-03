primeiro = int(input("Primeiro: "))
razao = int(input("Razao: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{} ".format(c), end=" → ")
print("Acabou")
