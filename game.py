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
    playButton = pygame.Rect(20, 30, 20, 10)

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
