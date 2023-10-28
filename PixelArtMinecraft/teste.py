import os
from PIL import Image
pasta = r"PixelArtMinecraft/blocos"
pasta_itens = os.listdir(pasta)
largura = len(pasta_itens)
altura = 1
x, y = 0, 0
imagem_inicial = Image.new("RGB", (largura*8, altura*8), (255, 255 ,255))
print(f"tamanho da imagem: largura: {largura*8}px; altura: {altura*8}px")
enumered_pasta = sorted(pasta_itens)
for k, item in enumerate(enumered_pasta):
    caminho_imagem = os.path.join(pasta, item)
    imagem = Image.open(caminho_imagem)
    imagem_aumentada = imagem.resize((8, 8))
    imagem_inicial.paste(imagem_aumentada, (x, y))
    x += 8
imagem_inicial.show()
