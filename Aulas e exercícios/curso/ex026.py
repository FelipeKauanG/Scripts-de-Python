#faca um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "a"
#em que posicao aparece a primeira vez
#em que posicao aparece na ultima vez

frase = str(input("Digite uma frase:")).strip().upper()

print("A letra '\033[0;36ma\033[m' aparece {} vezes\n"
      "\033[0;32mPrimeira posicao\033[m '{}'\n"
      "\033[0;31mUltima posicao\033[m {}".format(frase.count("A"), frase.find("A")+1, frase.rfind("A")+1))
