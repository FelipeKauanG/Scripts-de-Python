import matplotlib.pyplot as plt
import numpy as np


data = ["#646464",
"#4c4c4c",
"#392923",
"#4c4c4c",
"#575c5c",
"#4c4c4c",
"#646464",
"#664c33",
"#664c33",
"#4c3223",
"#191919"]

colors_rgb = [tuple(int(color[i:i+2], 16) / 255 for i in (1, 3, 5)) for color in data]

data = np.array(colors_rgb).reshape(1, len(data), 3)

plt.imshow(data, cmap="viridis")
plt.axis("off")
plt.show()
print(data)
