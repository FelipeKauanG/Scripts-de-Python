from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))

if idade == 18:
    print("Voce tem que se alistar imediatamente.")
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print("Voce ainda nao tem 18 anos, ainda faltam {} anos para o alistamento.".format(saldo))
    print("Seu alistamento sera em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print("Voce ja deveria ter se alistado ha {} anos.".format(saldo))
    print("Seu alistamento foi em {}..".format(ano))
