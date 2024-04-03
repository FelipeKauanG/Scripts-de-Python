tot18 = totH = totM20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: ")).upper().strip()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totH += 1
    if  sexo == "F" and idade < 20:
        totM20 += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
        print("-=-"*15)
    if resp == "N":
        break
print(f"Total de {tot18} pessoas com mais de 18 anos")
print(f"Ao todo temos {totH} homens cadastrados")
print(f"E temos {totM20} mulheres com menos de 20 anos")
