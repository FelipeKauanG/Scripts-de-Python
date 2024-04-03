import pyautogui as py
import random
from time import sleep

sleep(5)

texto = open("uteis\RoteirodoShrek.txt", "r+")



for palavra in texto.readlines():
    py.write(palavra)
    py.press("enter")


