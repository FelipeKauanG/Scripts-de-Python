from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil

from math import ceil


xpath = "/html/body/div[6]/div/div[8]/div/div[5]/div/div/div[2]/div/div/input[2]//div"

DFFs = []

pastaDFF = r"C:\\Users\\Felipe Kauan\\3D Objects\\GTA SA ALL DFFs"

pastaDestino = r"C:\\Users\\Felipe Kauan\\Desktop\\Nova pasta"

def excluirArquivos():
    pastaArquivo = os.listdir(pastaDestino)

    for arquivo in pastaArquivo:
        file = f"{pastaDestino}\\{arquivo}"
        shutil.rmtree(file)


excluirArquivos()



def pegarNomes():
    endereço = os.path.abspath(r"C:\\Users\\Felipe Kauan\\Desktop\\Mapa.html")

    driver = webdriver.Chrome()
    driver.get(endereço)

    className = "mp-item"

    elementos = driver.find_elements(By.CLASS_NAME,className)

    


    for elemento in elementos:
        nome = elemento.get_attribute("data-name")
        DFFs.append(f"{nome}.dff")

    print(f"Tem {len(elementos)} ao todo no site")

    driver.quit()

pegarNomes()



quantPastas = (ceil(len(DFFs)/50))
print(f"\033[96m{quantPastas} pastas\033[m")


Lista = []
def listarDffs():
    for arquivo in DFFs:
        caminho_arquivo = os.path.join(pastaDFF, arquivo)

        if os.path.isfile(caminho_arquivo):
            tamanho = os.path.getsize(caminho_arquivo)
            arquivo = (arquivo, tamanho)
            Lista.append(arquivo)

listarDffs()

listaNova = sorted(Lista, key=lambda x: x[1], reverse=True)


pasta_origem = "C:\\Users\\Felipe Kauan\\3D Objects\\GTA SA ALL DFFs"

pastaDestino = r"C:\\Users\\Felipe Kauan\\Desktop\\Nova pasta\\Parte"


quantArquivos = ceil(len(DFFs) / quantPastas)

def copiarDffs():
    indexPasta = 1
    atual = 0

    for arquivo in range(0, len(listaNova)):
        

        pastaAtual = f"{pastaDestino} {indexPasta}"


        os.makedirs(pastaAtual, exist_ok=True)

        caminho_origem = os.path.join(pasta_origem, listaNova[arquivo][0])

        caminho_destino = os.path.join(pastaAtual, listaNova[arquivo][0])

        shutil.copy(caminho_origem, caminho_destino)

        if atual == quantArquivos:
            atual = 0
            indexPasta += 1

        atual += 1
        
copiarDffs()
