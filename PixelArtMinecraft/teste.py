import matplotlib.pyplot as plt
import numpy as np


data = ['#646464', '#4c4c4c']

colors_rgb = [tuple(int(color[i:i+2], 16) / 255 for i in (1, 3, 5)) for color in data]

data = np.array(colors_rgb).reshape(1, len(data), 3)

plt.imshow(data)
plt.axis("off")
plt.show()
