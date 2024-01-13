import os
from PIL import Image
pasta = os.listdir(r"PixelArtMinecraft\blocos")
for bloco in pasta:
    print(f'\033[34m{bloco}\033[m'.replace(".png",""))

print(len(pasta))
