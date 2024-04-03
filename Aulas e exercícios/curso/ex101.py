# Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento
# de uma pessoa. retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, ou OBRIGATORIO
# nas eleicoes.
# voto opcional acima de 65 e abaixo de 18 anos, voto negado abaixo de 16 anos, e voto obrigatorio entre 18 e 64 anos

from datetime import date


# funcao
def voto(n):
    idade = date.today().year - n
    if 16 > idade:
        print(f"Com {idade} anos, o voto e NEGADO")
    elif 16 <= idade < 18 or idade > 65:
        print(f"Com {idade} anos, voto e OPCIONAL")
    else:
        print(f"com {idade} anos, o voto e OBRIGATORIO")


# programa principal
voto(int(input("Em que ano voce nasceu ?")))
