# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre - os(com idade)
# em um dicionario se por acaso a cetps for diferente de ZERO, o dicionario recebera tambem o ano de
# contratacao e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
# considere - se que a pessoa se aposentaa apos 35 anos de colaboracao
import datetime
dados = {}
while True:
    dados["Nome"] = str(input("Nome: ")).strip().title()
    dados["Idade"] = datetime.datetime.today().year - int(input("Ano de Nascimento: "))
    dados["CTPS"] = int(input("Carteira de Trabalho (0 nao tem): "))
    if dados["CTPS"] == 0:
        for p, y in dados.items():
            print(f"{p} tem o valor {y}")
        break
    else:
        dados["Contr"] = int(input("Ano de contratacao: "))
        dados["Salario"] = float(input("Salario: "))
    print("-=-"*15)
    for p, y in dados.items():
        print(f"{p} tem o valor {y}")
    print(f"Aposentadoria tem o valor {dados['Contr'] + 35 - (datetime.datetime.today().year - dados['Idade'])}")
    break
