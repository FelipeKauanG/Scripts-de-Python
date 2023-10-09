from PIL import Image

imagem = Image.open(r"úteis\Normais\Pillow\jacket.png")

largura, altura = imagem.size

print(largura, altura)
