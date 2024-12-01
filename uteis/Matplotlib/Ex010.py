from matplotlib import pyplot as plt
import numpy as np

np.random.seed(100)
x = np.random.normal(1, 2,100)

plt.hist(x)
plt.show()