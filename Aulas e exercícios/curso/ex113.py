# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma finalidade.

def leiaInt(texto):
    try:
        texto = str(input("Digite um número inteiro: ")).strip()
        while not int(texto.isnumeric()) or int(texto) % 1 != 0 or len(texto) == 0:
            texto = str(input("\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m")).strip()
    except KeyboardInterrupt:
        print("\n\033[0;31mO usuário preferiu não informar os valores.\033[m")
    return texto


def leiaFloat(texto):
    try:
        texto = str(input("Digite um número real: ")).strip()
        while float(texto.isalpha()) or float(texto.isalnum()) or len(texto) == 0:
            texto = str(input("\033[0;31mERRO: por favor, digite um número real válido.\033[m")).strip()
    except KeyboardInterrupt:
        print("\n\033[0;31mO usuário preferiu não informar os valores.\033m")
    return texto


inteiro = leiaInt("0")
real = leiaFloat("0")
print(f"\033[0;36mVocê digitou o valor inteiro {inteiro}, e o valor real foi {real}\033[m")
