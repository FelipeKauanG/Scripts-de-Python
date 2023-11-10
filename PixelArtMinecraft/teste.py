from PIL import Image
img = Image.open(r"/home/felipe/Imagens/Textures/painting/fire.png")
img = img.convert("RGB")
largura, altura = img.size

for larg in range(0, largura //2):
    for altu in range(0, altura //2):
        print(f"{img.getpixel((larg,altu))}")
print(largura * altura)
