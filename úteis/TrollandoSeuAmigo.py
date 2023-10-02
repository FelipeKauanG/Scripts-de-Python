import pyautogui as py
import random
import time
time.sleep(5)

mensagens = ["tá doidão", "Tudo certo", "E aí", "Partiu", "COÉ", "Eita, Preula", "TMJ", "Eh Nóis"]

for i in range(50):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")