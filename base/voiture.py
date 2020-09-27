import pygame
from pygame.locals import *

class Voiture():
    def __init__(self):
        self.sprite = pygame.image.load("Enemy.png")
        self.posX = 200
        self.posY = 200
