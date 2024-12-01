import matplotlib.pyplot as plt

# Função para desenhar o mosaico de quadrados
def desenhar_mosaico(x, y):
    # Tamanho de cada quadrado
    tamanho_quadrado = 1

    # Criar uma matriz de zeros para representar o mosaico
    mosaico = [[0] * x for _ in range(y)]

    for i in range(x):
        for j in range(y):
            # Alterna as cores dos quadrados com base nas coordenadas (i, j)
            if (i + j) % 2 == 0:
                mosaico[j][i] = 1

    # Desenhar o mosaico
    plt.imshow(mosaico, cmap='gray', aspect='equal')
    plt.axis('off')
    plt.show()

# Valores de x e y (número de quadrados nas direções x e y)
x = 8
y = 6

desenhar_mosaico(x, y)
