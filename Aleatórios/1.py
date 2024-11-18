def Criptografar():
    preAlfabeto = "abcdefghijklmnopqrstuvwxyz"
    posAlfabeto = []

    palavra = "MAMACO".lower().replace(" ", "").replace(",", "") #str(input("Digite uma palavra AGORA: "))

    for i in range(0, len(preAlfabeto)):
        posAlfabeto.append(preAlfabeto[i])


    for letra in range(0, len(palavra)):
        print(posAlfabeto.index(palavra[letra])+1, end="")


Criptografar()
