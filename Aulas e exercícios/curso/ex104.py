# Crie um programa que tenha a funcao chamada leiaInt(), que vai funcionar de forma semelhante a
# funcao input() do Python, so que fazendo a validacao para aceitar apenas um valor numerico.
# EX: n = leiaInt("Digite um numero").

def leiaint(entrada):
    entrada = str(input(entrada).strip())
    while not int(entrada.isnumeric()) or int(entrada) % 1 != 0:
        entrada = str(input("\033[0;31mERRO, tente novamente com um numero inteiro!\033[m"))
    return entrada


n = leiaint("Digite um numero")
print(f"\033[0;36mVoce digitou o numero {n}\033[m")
