import pyautogui as pag
from random import randint
from time import sleep

sleep(3)
x = 1440
y = 900
delay = 0.2

pag.moveTo(x/2, y/2, 0, pag.easeInOutCirc)

triangulo = 200
while True:
    pag.moveTo(x/2, y/2-triangulo, delay, pag.easeInOutCirc)
    pag.moveTo(x/2-triangulo, y/2+triangulo, delay, pag.easeInOutCirc)
    pag.moveTo(x/2+triangulo, y/2+triangulo, delay, pag.easeInOutCirc)
