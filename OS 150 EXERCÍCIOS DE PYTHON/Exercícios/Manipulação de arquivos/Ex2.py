# 2 - Escreva um programa que leia um arquivo de texto e exiba o número de palavras, o número de linhas e o tamanho total do arquivo em bytes.

texto = open(mode="r", file=r'OS 150 EXERCÍCIOS DE PYTHON\Exercícios\Manipulação de arquivos\Ex02 Documentos\texto.txt')
#print(str(texto.readlines()).replace(" ", "").replace(r"\n", "").replace(",", " ").replace("''", "").replace(".", " "))

textoSplit = (str(texto.readlines())) #palavras

#print(f"O texto tem {len(str(textoSplit).split(' '))} palavras\nTem também {len(str(textoSplit))} linhas!")

