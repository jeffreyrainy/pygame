import pygame
from pygame.locals import *

class Game():
    def __init__(self):

        self.done = False
        pygame.init()
        self.clockFPS = pygame.time.Clock()
        self.displaySurf = pygame.display.set_mode((800, 600))
        self.sprite = pygame.image.load("Enemy.png")
        self.posX = 200
        self.posY = 200

    def events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.done = True

        self.pressed_keys = pygame.key.get_pressed()

    def update(self):

        if self.pressed_keys[K_LEFT]:
            self.posX = self.posX - 5
        if self.pressed_keys[K_RIGHT]:
            self.posX = self.posX + 5

        self.clockFPS.tick(30)

    def display(self):

        self.displaySurf.fill((0, 0, 0))
        self.displaySurf.blit(self.sprite, (self.posX, self.posY))
        pygame.display.update()

    def quit(self):

        pygame.quit()

