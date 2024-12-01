from matplotlib import pyplot as plt

y = []
x =[]
for i in range(1, 11):
    x.append(i**2)
    y.append(i)

plt.plot(x , y)
plt.grid(color ='#000000', linestyle ='-', linewidth =0.5)

plt.show()