#Faca um programa que leia nome e media de um aluno, guardando tambem em um dicionario.
#No final, mostre o conteudo da estrutura na tela.
# aprovado: maior ou igual a 7
# reprovado: abaixo de 7

dados = {}
dados["Nome"] = str(input("Nome: ")).title().strip()
dados["Media"] = float(input(f"Media de {dados['Nome']}: "))

print(f"Nome e igual a {dados['Nome']}")
print(f"Media e igual a {dados['Media']}")
if dados['Media'] >= 7:
    print("Situacao e igual a \033[0;34mAprovado\033[m")
elif 5 < dados['Media'] < 7:
    print("Situacao e igual a \033[0;33mRecuperacao\033[m")
else:
    print("Situacao e igual a \033[0;31mreprovado\033[m")
