import pygame
from pygame.locals import *

class Voiture():
    def __init__(self, keys):
        self.sprite = pygame.image.load("Enemy.png")
        self.posX = 200
        self.posY = 200
        self.keys = keys

    def move(self, keys):

        if keys[self.keys[0]]:
            self.posX = self.posX - 5
        if keys[self.keys[1]]:
            self.posX = self.posX + 5
        if keys[self.keys[2]]:
            self.posY = self.posY - 5
        if keys[self.keys[3]]:
            self.posY = self.posY + 5

