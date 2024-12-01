from matplotlib import pyplot as plt
from random import randint

idade = []
x = []
for num in range(1, 20):
    idade.append(randint(1, 101))
    x.append(num)
print(idade)
plt.xlabel("Quantidade")
plt.ylabel("Idade")
plt.plot(x, idade)
plt.show()
