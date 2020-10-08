import pygame
from pygame.locals import *

class Voiture():
    def __init__(self, posX, posY):
        self.sprite = pygame.image.load("Enemy.png")
        self.posX = posX
        self.posY = posY
        
