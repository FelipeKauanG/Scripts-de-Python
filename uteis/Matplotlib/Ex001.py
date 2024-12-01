from matplotlib import pyplot as plt
from random import randint

x = []
y = []
for X in range(1, 13):
    x.append(randint(100000, 500000))
    y.append(X)

plt.plot(y, x)
plt.show()
