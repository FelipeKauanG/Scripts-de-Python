from random import randint

cores = []

for i in range(0, 101):
    cor = f"cor {(randint(1,100))}"
    cores.append(cor)
    
def extrairnumero(cor):
    return int(cor.split()[1])

cores = sorted(cores, key=extrairnumero)

print(cores)
