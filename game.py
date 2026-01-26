import time
import displayio
import terminalio
from adafruit_display_text import label
from blinka_displayio_pygamedisplay import PyGameDisplay

import pygame
import os
import random
from sys import exit

display = PyGameDisplay(width=128, height=128)

splash = displayio.Group()
display.root_group = splash
text = "hackapet stuff"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=64)
splash.append(text_area)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    time.sleep(0.1)