#Programado por GM_Senpai

from PIL import Image

import pyautogui as py

from time import sleep

from colormap import rgb2hex

branco1 = range(0,31)

imagem = Image.open('Imagem Yamcha.png')
rgb = imagem.convert('RGB')

sleep(5)

for x in range(295, 801):
    for y in range(226, 639):
        cor = rgb.getpixel((x, y))
        for branco in branco1:
            if cor == (branco, branco, branco):
                py.click(x=x, y=y, button='left')
        if cor == (152, 152, 152) or cor == (151, 151, 151) or cor == (79, 79, 79) or cor == (86, 86, 86):
            py.click(x=x, y=y, button='left')
