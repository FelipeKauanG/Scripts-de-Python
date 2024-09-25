import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

# Constantes
a0 = 1.0  # Usamos unidades naturais onde o raio de Bohr é 1

# Parte radial da função de onda (n=2, l=1)
def R_21(r):
    return (1 / np.sqrt(2)) * (1 / a0**(3/2)) * (r / a0) * np.exp(-r / (2 * a0))

# Harmônico esférico Y_10 (l=1, m=0)
def Y_10(theta, phi):
    return np.sqrt(3 / (4 * np.pi)) * np.cos(theta)

# Função de onda completa psi_210 em coordenadas esféricas
def psi_210(r, theta, phi):
    return R_21(r) * Y_10(theta, phi)

# Criação de uma grade esférica
r = np.linspace(0, 10, 200)  # distância radial
theta = np.linspace(0, np.pi, 200)  # ângulo polar
phi = np.linspace(0, 2*np.pi, 200)  # ângulo azimutal

# Grade de coordenadas
r, theta, phi = np.meshgrid(r, theta, phi)

# Conversão para coordenadas cartesianas para visualização
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Cálculo da densidade de probabilidade |ψ(r,θ,φ)|^2
psi = psi_210(r, theta, phi)
prob_density = np.abs(psi)**2

# Visualização 3D da densidade de probabilidade
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter(x, y, z, c=prob_density, cmap='viridis', marker='o', alpha=0.6)

# Adiciona uma barra de cores para indicar a densidade de probabilidade
cbar = fig.colorbar(img, ax=ax, pad=0.1)
cbar.set_label('Densidade de Probabilidade')

# Labels e título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'Densidade de Probabilidade $|\psi_{210}(r,\theta,\phi)|^2$')

plt.show()
