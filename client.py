# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:06:23 2020

@author: nguye
"""

import pygame
from tkinter import *

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    