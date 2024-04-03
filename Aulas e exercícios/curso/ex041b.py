from datetime import date

atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print("O atleta tem {} anos.".format(idade))

if idade <= 9:
    print("Classificacao: MIRIM")
elif idade <= 14:
    print("Classificacao: INFANTIL")
elif idade <= 19:
    print("Classificacao: JUNIOR")
elif idade <= 25:
    print("Classificacao: SENIOR")
else:
    print("Classificacao: MASTER")
