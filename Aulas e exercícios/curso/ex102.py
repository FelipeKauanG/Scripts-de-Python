# crie um programa que tenha uma funcao fatorial() que receba dois parametros: o primeiro que indique
# o numero a calcular e o outro chamado show, que sera um valor logico (opcional) indicado se sera mostrado
# ou nao na tela o processo de calculo do fatorial.

def fatorial(f=1, show=False):
    """
    → Faz o calculo de um valor com fatorial
    :param f: E o número do fatorial que vai ser calculado
    :param show: E um valor booleano(verdadeiro ou falso) que vai configurar se vai mostrar o passo a passo ou nao
    :return:Valor do fatorial de um numero (n).
    Criado por Felipe
    """
    cont = 1
    if show:
        for f in range(f, 1, -1):
            cont *= f
            print(f"{f} x ", end="")
        print(f"{1} = {cont}")
    else:
        for f in range(f, 1, -1):
            cont *= f
        print(cont)


fatorial(0, show=True)
