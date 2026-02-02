import time
import displayio
import terminalio
from adafruit_display_text import label
from blinka_displayio_pygamedisplay import PyGameDisplay

import pygame
import os
import random
from sys import exit

gameWidth = 128
gameHeight = 128
score = 0
gameState = "start"
player = pygame.Rect(40,25,0,10)
isPlaying = True

display = PyGameDisplay(width=gameWidth, height=gameHeight)
pygame.display.set_caption("game")

splash = displayio.Group()
display.root_group = splash
text = "score:" + str(score)
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=64)
splash.append(text_area)

def startGame():
    playerBitmap = displayio.Bitmap (128, 128, 1)
    playerPalette = displayio.Palette(1)
    playerPalette[0] = 0x0FFFF
    playerTile = displayio.TileGrid(playerBitmap, pixel_shader=playerPalette, x=0, y=0)


def draw():
    if gameState == "start":
        startGame()

def loadImages():
    images = {}
    for fileName in os.listdir("assets/"):
        if fileName.endswith('.png'):
            path = os.path.join("assets/", fileName)
            image = pygame.image.load(path).convert_alpha()
            key = os.path.splitext(fileName)[0]
            images[key] = image
    return images

image = loadImages()

while isPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw()
    display.refresh()
    time.sleep(0.1)
