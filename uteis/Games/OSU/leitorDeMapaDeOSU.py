from time import sleep 
import pygame
import os

#Caminho do arquivo .osu
musica = r"VINXIS - Sidetracked Day (DendyHere) [Infinity Inside].osu"

pasta = r"838182 VINXIS - Sidetracked Day"

path = r"C:\Users\Felipe Kauan\AppData\Local\osu!\Songs"

link = os.path.join(path, pasta, musica)

#print(f"\n\033[35m{link}\033[m")


#inicializar o pygame
pygame.init()



#Ler o arquivo .osu
try:
    with open(link, mode="r", encoding="utf-8") as mapa:
        conteudo = mapa.read()

except FileNotFoundError:
    print(f"\033[31mAquivo \033[35mOSU!\033[m\033[31m não encontrado!\033[m")
    exit()


#Pegar o hitObjects
try:
    hitObjects = conteudo.split("[HitObjects]")[1].strip().split("\n")


except IndexError:
    print("\033[31mErro ao locallizar HitObjects no mapa.\033[m")


#Som para o beat
beat__path = os.path.join(path, pasta)


nomeAudio = ""

#Verifica o dtipo de arquivo, se é .ogg ou .mp3
for item in os.scandir(beat__path):

    if item.name.endswith(".mp3") or item.name.endswith(".ogg"):
        nomeAudio = item.name


#Caminho completo do audio
audio = os.path.join(beat__path, nomeAudio)

#Volumes:
volMusica = 1
volBeat = 0.5

#Carrega o beat da música
beat_sound = pygame.mixer.Sound(r"uteis\Games\OSU\beat\beat.ogg")
beat_sound.set_volume(volBeat)


#Função tocar música
def tocarMusica(dt=False):
    sleepNum = 0
    print(f"\033[34mTocando: {musica}\033[m")

    #Carrega a música
    pygame.mixer.music.load(audio)
    pygame.mixer.music.set_volume(volMusica)
    pygame.mixer.music.play()

    #executa cada linha do hitObjects e transforma em ritmo
    for linha in enumerate(hitObjects):
        
        ms = int(linha[1].split(",")[2]) - int(sleepNum)

        sleepNum = linha[1].split(",")[2]
        
        ms = abs(ms/1000)

        #Faz o beat
        if linha[0] != 0:
            beat_sound.set_volume(0.5)
            beat_sound.play()
            print(f"\033[32m-{linha[0]}\033[m")

        sleep(ms)
        


tocarMusica()

#Enquanto o programa é executado, espera 1ms
while pygame.mixer.music.get_busy():
    sleep(1)

