#Faca um programa que leia o sexo de um pessoa, mas so aceite os valores "F" ou "M".
#Caso esteja errado, peca a digitacao novamente ate ter um valor correto.


sexo = str(input("Digite o seu sexo [F/M]")).lower()

while sexo != str("f") or sexo != str("m"):
    sexo = str(input("Valor incorreto, digite [F/M]!")).lower()
print("Fim")
