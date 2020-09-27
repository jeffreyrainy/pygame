import pygame
from pygame.locals import *
from voiture import Voiture 

class Game():
    def __init__(self):

        self.done = False
        pygame.init()
        self.clockFPS = pygame.time.Clock()
        self.displaySurf = pygame.display.set_mode((800, 600))
        self.v1 = Voiture()
        self.v2 = Voiture()
    def events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.done = True

        self.pressed_keys = pygame.key.get_pressed()

    def update(self):

        if self.pressed_keys[K_LEFT]:
            self.v1.posX = self.v1.posX - 5
        if self.pressed_keys[K_RIGHT]:
            self.v1.posX = self.v1.posX + 5
        if self.pressed_keys[K_UP]:
            self.v1.posY = self.v1.posY - 5
        if self.pressed_keys[K_DOWN]:
            self.v1.posY = self.v1.posY + 5
        
        if self.pressed_keys[K_a]:
            self.v2.posX = self.v2.posX - 5
        if self.pressed_keys[K_d]:
            self.v2.posX = self.v2.posX + 5
        if self.pressed_keys[K_w]:
            self.v2.posY = self.v2.posY - 5
        if self.pressed_keys[K_s]:
            self.v2.posY = self.v2.posY + 5

        self.clockFPS.tick(30)

    def display(self):

        self.displaySurf.fill((0, 0, 0))
        self.displaySurf.blit(self.v1.sprite, (self.v1.posX, self.v1.posY))
        self.displaySurf.blit(self.v2.sprite, (self.v2.posX, self.v2.posY))
        pygame.display.update()

    def quit(self):

        pygame.quit()

