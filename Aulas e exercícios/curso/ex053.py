#Crie um programa que leia uma frase qualquer e diga se ela e um palindromo,
# desconsiderando os espacos #ex palindromo

print("Analizador de palindromos.")
frase = str(input("Digite uma frase: ")).strip().upper()
inverso = frase[::-1]
junto = "".join(frase)
print(inverso)
if frase == inverso:
    print("Temos um palindromo!!!")
else:
    print("Nao temos um palindromo")
