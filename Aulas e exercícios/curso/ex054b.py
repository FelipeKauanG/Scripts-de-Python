from datetime import date

atual = date.today().year
totmenor = 0
totmaior = 0
for pess in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu? ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        print("Essa pessoa e maior")
    else:
        print("Essa pessoa e menor")
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("Ao todo tivemos {} pessoas menores de idade".format(totmenor))
