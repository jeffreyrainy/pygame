import pygame
from pygame.locals import *
from voiture import Voiture 

class Game():
    def __init__(self):

        self.done = False
        pygame.init()
        self.clockFPS = pygame.time.Clock()
        self.displaySurf = pygame.display.set_mode((800, 600))
        self.v1 = Voiture((K_LEFT, K_RIGHT, K_UP, K_DOWN))
        self.v2 = Voiture((K_a, K_d, K_w, K_s))
    def events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.done = True

        self.pressed_keys = pygame.key.get_pressed()

    def update(self):

        self.v1.move(self.pressed_keys)
        self.v2.move(self.pressed_keys)
        
        self.clockFPS.tick(30)

    def display(self):

        self.displaySurf.fill((0, 0, 0))
        self.displaySurf.blit(self.v1.sprite, (self.v1.posX, self.v1.posY))
        self.displaySurf.blit(self.v2.sprite, (self.v2.posX, self.v2.posY))
        pygame.display.update()

    def quit(self):

        pygame.quit()

