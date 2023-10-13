from matplotlib import pyplot as plt
from random import randint

vendas = []
x = []
for i in range(1, 10):
    x.append(i)
    vendas.append(randint(1, 10))

plt.bar(x, vendas)
plt.show()
