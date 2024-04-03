from datetime import date

ano = int(input("Que ano quer analizar? Coloque 0 para analizar o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} e \033[0;32mbissexto\033[m".format(ano))
else:
    print("O ano de {} nao e \033[0;33mbissexto\033[m".format(ano))
