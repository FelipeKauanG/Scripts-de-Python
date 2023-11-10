import os
import sys

colors = {"Grass": "127, 178, 56", "Sand":"247, 233, 163", "wool": "199, 199, 199", "Redstone_block": "255, 0, 0", "Ice": "160, 160, 255", "Metal": "167, 167, 167", "cactus": "0, 124, 0", "Snow": "255, 255, 255", "Clay": "164, 168, 184", "Dirt": "151, 109, 77", "Stone": "112, 112, 112", "Water": "64, 64, 255", "Wood": "143, 119, 72", "Quartz": "255, 252, 245", "acacia_planks": "216, 127, 51", "Color_magenta" : "178, 76, 216", "Color_light_blue": "102, 153, 216", "Color_yellow": "229, 229, 51", "Color_light_green": "127, 229, 51", "Color_pink": "242, 127, 165", "gray_wool": "76, 76, 76", "Color_light_gray": "153, 153, 153", "Color_cyan": "76, 127, 153", "Color_purple": "127, 63, 178", "Color_blue": "51, 76, 178", "Color_brown": "102, 76, 51", "Color_green": "102, 127, 51", "Color_red": "153, 51, 51", "Color_black": "25, 25, 25", "Gold":"250, 238, 25", "Diamond": "92, 219, 213", "Lapis": "74, 128, 255", "Emerald": "0, 217, 58", "Spruce": "129, 86, 49", "Nether": "112, 2, 0", "Terracotta_white": "209, 177, 161", "Terracotta_orange": "159, 872, 36", "Terracotta_magenta": "149, 87, 108","Terracotta_light_blue": "112, 108, 138", "Terracotta_yellow": "186, 133, 36", "Terracotta_light_green": "103, 117, 53", "Terracotta_pink": "160, 77, 78", "Terracotta_gray": "57, 41, 35", "Terracotta_light_gray": "137, 107, 98","Terracotta_cyan": "87, 92, 92", "Terracotta_purple": "122, 73, 88", "Terracotta_blue": "76, 62, 92", "Terracotta_brown": "76, 50, 35","Terracotta_green": "76, 82, 42", "Terracotta_red": "142, 60, 46", "Terracotta_black": "37, 22, 16","Crimson_nylium":"189, 48, 49","Crimson_hyphae":"92, 25, 29","Crimsom_stem":"148, 63, 97", "Warped_nylium" : "22, 126, 134","Warped_stem":"58, 142, 140","Warped_hyphae":"86, 44, 62","Warped_wart_block":"20, 180, 133","Deepslate":"100, 100, 100","Raw_iron":"216, 175, 147", "verdant_froglight_top":"127, 167, 150"}

pasta = os.listdir(r"PixelArtMinecraft/blocos")
#print(pasta)


for bloco in pasta:
    nome_bloco = os.path.splitext(bloco)[0]
    if nome_bloco in colors:
        print(f"\033[32mBloco {nome_bloco}\033[m")
    else:
        print(f"\033[31mBloco {nome_bloco}\033[m")
        
print(len(colors.keys()))