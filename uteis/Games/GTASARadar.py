import PIL as pil
import os
from PIL import Image

# Listando arquivos na pasta
pasta = os.listdir("../../../../../Desktop/Radar")
novaPasta = []
for img in range(0, len(pasta)):
    if img < 10:
        novaPasta.append(f"radar0{img}.png")
    else:
        novaPasta.append(f"radar{img}.png")


def mostrarIMG():
    # Lista de imagens
    images = []
    tamanho = (512, 512)  # Tamanho de cada imagem

    # Criando uma imagem grande para colar as imagens menores
    res = Image.new("RGBA", (tamanho[0] * 12, tamanho[1] * 12), color="white")

    linha = 0
    coluna = 0

    for bloco in range(0, len(novaPasta)):
        img_path = f"../../../../../Desktop/Radar/{novaPasta[bloco]}"

        # Certificando-se de que o arquivo existe
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize(tamanho)  # Redimensiona a imagem para o tamanho correto

            # Colando a imagem na posição correta
            res.paste(img, (coluna * tamanho[0], linha * tamanho[1]))

            # Atualiza a coluna e a linha para a próxima imagem
            coluna += 1
            if coluna >= 12:  # Quando a coluna chegar ao final, pula para a próxima linha
                coluna = 0
                linha += 1

    # Exibindo a imagem final
    res.show()
    # Salvando a imagem final com um nome específico
    res.save("../../../../../Desktop/Radar/imagem_final.png")


mostrarIMG()
