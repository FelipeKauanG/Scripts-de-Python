# Faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar
# um dicionario com as seguintes informacoes:

# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situacao (opcional(boa, ruim, etc...))
# Adicione tambem as docstrings da funcao.
def notas(*num, sit=False):
    """
    → Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicnado se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação de turma.
    """
    dados = dict()
    dados["Nota maior"] = max(num)
    dados["Nota menor"] = min(num)
    dados["Media"] = sum(num) / len(num)
    if sit:
        if dados['Media'] < 5:
            dados['Situação'] = "\033[0:31mRuim\033[m"

        elif dados['Media'] >= 7:
            dados['Situação'] = "\033[0:32mBoa\033[m"

        else:
            dados['Situação'] = "\033[0:33mRecuperação\033[m"
    for k, v in dados.items():
        print(f"\033[0:35m{k}\033[m é igual a {v}")
    return num


resp = notas(10, 5, sit=True)
