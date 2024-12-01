from matplotlib import pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=20)

plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.title("Histograma com Rótulos")

#Adicionando rótulos para os intervalos
plt.xticks(np.arange(min(data), max(data)+1, 0.5))

plt.show()