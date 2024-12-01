import matplotlib.pyplot as plt
clima = [24.7, 24.9, 24.3, 23.5, 21, 20.4, 20.6, 22.5, 24.5, 25.5, 24.6, 24.8]
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.bar(y, clima)
plt.xlabel(meses)
