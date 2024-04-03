#Faca um programa que tenha a funcao chamada escreva(),
# que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel.
#Ex:
#escreva("Ola, mundo!")
#Saida:
#-----------
#Ola, mundo!
#-----------


def escreva(txt):
    print("-"*(len(txt)+4))
    print(f"  {txt}")
    print("-"*(len(txt)+4))
    print()


escreva("Gustavo Guanabara")
escreva("Curso de Python no youTube")
escreva("CEV")
