from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

labels = ["Ponto 1", "Ponto 2", "Ponto 3", "Ponto 4", "Ponto 5"]

plt.scatter(x, y)
for i, label in enumerate(labels): #Coloca annotate labels para x e y enumerados com o labels que escrevemos "Ponto 1, etc"
    plt.annotate(label, (x[i], y[i]))


plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de Dispersão com Rótulos")
plt.show()