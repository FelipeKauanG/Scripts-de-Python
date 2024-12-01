from matplotlib import pyplot as plt
from random import randint

x = []
y = []

for i in range(1, 21):
    x.append(randint(1, 100))
    y.append(i)

plt.scatter(x, y)
plt.show()