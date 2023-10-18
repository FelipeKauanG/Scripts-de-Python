import numpy as np

tabela = r"""Disciplina 1º Bimestre 2º Bimestre 3º Bimestre 4º Bimestre CF
N F AC %Freq N F AC %Freq N F AC %Freq N F AC %Freq N F AC
ARTE 4 - - 0% 5 3 - 0% 5 2 - 0% 5 - - 0% 5 5 -
CIENCIAS FISICAS E BIOLOGICAS 5 1 - 0% 6 - - 0% 6 1 - 0% 6 - - 0% 6 2 -
EDUCACAO FISICA 8 1 - 0% 8 2 - 0% 10 1 - 0% 8 2 - 0% 8 6 -
GEOGRAFIA 7 1 - 0% 8 5 - 0% 8 2 - 0% 6 - - 0% 7 8 -
HISTORIA 8 2 - 0% 6 1 - 0% 6 6 - 0% 7 1 - 0% 6 10 -
LINGUA ESTRANGEIRA INGLES 9 1 - 0% 5 3 - 0% 9 4 - 0% 7 1 - 0% 8 9 -
LINGUA PORTUGUESA 8 2 - 0% 7 8 - 0% 9 2 - 0% 7 - - 0% 8 12 -
MATEMATICA 8 1 - 0% 7 5 - 0% 8 7 - 0% 8 2 - 0% 8 15 -"""

tabelaTratada = []
tabela = tabela.split()
total = int(len(tabela)/4)

tabela = np.reshape(tabela,[4, total])

print(tabela)

