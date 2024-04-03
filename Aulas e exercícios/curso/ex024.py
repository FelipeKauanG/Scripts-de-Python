#Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo"

cid = str(input("Qual o nome de uma cidade ?")).strip()
ver = cid.find(" ")

print("""\033[0;31mSua cidade comeca com "Santo" no nome\033[m \n\n{}""".format("Santo" in cid[:-ver]))
