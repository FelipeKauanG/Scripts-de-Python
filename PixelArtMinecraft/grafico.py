from PIL import Image
import os

bloco = os.listdir(r"PixelArtMinecraft\blocos")
blocoSelecionado = bloco[3]

ImagemBloco = Image.open(os.path.join(r"PixelArtMinecraft\blocos", blocoSelecionado))

largura = 64
altura = 64

imagem = Image.new("RGB", (largura, altura), color="white")
imagem.paste(ImagemBloco, (altura//2, largura//2))

imagem.show()
