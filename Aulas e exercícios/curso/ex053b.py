frase = str(input("Digite um frase: ")).strip().upper() #.strip e .upper para tirar espacos e tornar elas maiusculas
palavras = frase.split() #esplitar uma frase em pedacos
junto = "".join(palavras) #juntar palavras com o .join
print("Voce digitou a frase {}".format(junto)) #mostrar a frase
inverso = "" #inverso sendo vazio
for letra in range(len(junto) - 1, -1, -1): #revertendo a frase
    inverso += junto[letra] #adicionar a variavel inverso com a variavel junto com a frase invertida
print("O inverso de {} e {}".format(junto, inverso)) #mostrando a palavra normal e o inverso da frase
if inverso == junto:
    print("Temos um palindromo")
else:
    print("A frase digitada nao e um palindromo")
