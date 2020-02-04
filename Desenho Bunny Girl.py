# Programado por GM_Senpai

from PIL import Image

import pyautogui as py

from time import sleep
from time import time

#Imagem com 510x420
imagem = Image.open('bunny girl.png')
rgb = imagem.convert('RGB')

sleep(3)



def remove(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort(reverse=True)
    return l


inicio = time()

color = []
for x in range(0, 510):
    for y in range(0, 420):
        cor = rgb.getpixel((x, y))
        if cor != (255, 255, 255):
            color.append(cor)

lista = remove(color)

for i in lista:
    escala = int((i[0] / 2.55) - 100) * -1
    if (i != (255, 255, 255) or i !=(0,0,0)):
        py.click(233, 407, button='left')
        py.click(427, 436 + escala, button='left')
        py.click(620, 629)
        sleep(1)
    for x in range(0, 510):
        for y in range(0, 420):
            cor = rgb.getpixel((x, y))

            if cor != (255, 255, 255) and i == cor:
                #de onde começa a tela de desenho 302x144
                py.click(x+302, y+144, button='left')

fim = time()

print(fim - inicio)