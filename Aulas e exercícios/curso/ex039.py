#Faca um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#se ele ainda vai se alistar.
#se e a hora de se alistar
#se ja passou do prazo de se alistar
# seu programa devera tambem mostrar o tempo que falta ou que passou do prazo

from datetime import date

data = int(input("informe seu ano de nascimento: "))
idade = date.today().year - data



if idade < 18:
    print("Ainda \033[0;33mnao esta na hora de se alistar\033[m, restam {} ano(s)".format(18-idade))
elif idade == 18:
    print("Esse ano \033[0;32mpode se alistar\033[m para o exercito")
else:
    print("Ja \033[0;031mpassou do prazo\033[m de se alistar, se passaram {} ano(s)".format(idade - 18))
