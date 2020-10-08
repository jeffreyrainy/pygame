import pygame
from pygame.locals import *
from voiture import Voiture 

class Game():
    def __init__(self):

        self.done = False
        pygame.init()
        self.clockFPS = pygame.time.Clock()
        self.displaySurf = pygame.display.set_mode((800, 600))
        self.v1 = Voiture(200, 200)
        self.v2 = Voiture(200, 400)
    def events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.done = True

        self.pressed_keys = pygame.key.get_pressed()

    def clip(self, x, y, sprite):
        if x < 0 :
            x = 0
        if y < 0:
            y = 0
        limitX = self.displaySurf.get_width() - sprite.get_width()
        if x > limitX:
            x = limitX
        limitY = self.displaySurf.get_height() - sprite.get_height()
        if y > limitY :
            y = limitY
        return (x, y)

    def update(self):

        x = self.v1.posX
        y = self.v1.posY

        if self.pressed_keys[K_LEFT]:
            x = self.v1.posX - 15
        if self.pressed_keys[K_RIGHT]:
            x = self.v1.posX + 15
        if self.pressed_keys[K_UP]:
            y = self.v1.posY - 15
        if self.pressed_keys[K_DOWN]:
            y = self.v1.posY + 15

        (x, y) = self.clip(x, y, self.v1.sprite)

        self.v1.posX = x
        self.v1.posY = y
        
        if self.pressed_keys[K_a]:
            self.v2.posX = self.v2.posX - 15
        if self.pressed_keys[K_d]:
            self.v2.posX = self.v2.posX + 15
        if self.pressed_keys[K_w]:
            self.v2.posY = self.v2.posY - 15
        if self.pressed_keys[K_s]:
            self.v2.posY = self.v2.posY + 15

        self.clockFPS.tick(30)

        

    def display(self):

        self.displaySurf.fill((0, 0, 0))
        self.displaySurf.blit(self.v1.sprite, (self.v1.posX, self.v1.posY))
        self.displaySurf.blit(self.v2.sprite, (self.v2.posX, self.v2.posY))
        pygame.display.update()

    def quit(self):

        pygame.quit()

