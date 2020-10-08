import pygame
from pygame.locals import *

class Game():
    def __init__(self):
        from voiture import Voiture 

        self.done = False
        pygame.init()
        self.clockFPS = pygame.time.Clock()
        self.displaySurf = pygame.display.set_mode((800, 600))

        self.v1 = Voiture((200, 200), (K_LEFT, K_RIGHT, K_UP, K_DOWN), self)
        self.v2 = Voiture((200, 400), (K_a, K_d, K_w, K_s), self)

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

