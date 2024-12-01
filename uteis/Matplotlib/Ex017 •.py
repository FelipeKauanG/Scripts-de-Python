from matplotlib import pyplot as plt
import numpy

x = numpy.random.rand(50)
y = numpy.random.rand(50)

plt.scatter(x, y)
z = numpy.polyfit(x, y, 1)
p = numpy.poly1d(z)

plt.plot(x, p(x), "r--")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("GRáfico de Dispersão com linha de Tendência")

plt.show()
