#Faca um programa que ultilize o Interactive Help do Python.
# O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra "FIM",
# o programa se encerra.
#OBS: use cores.

print("\033[0:102:30mSISTEMA DE AJUDA PyHELP\033[m")
while True:

    func = str(input("\033[0:107:30mFunção ou biblioteca: \033[m")).strip().lower()
    if func == "fim":
        break
    print(f"{help(func)}")
print("\033[0:101:30mPrograma finalizado\033[m")
