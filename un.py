import pygame, sys
from pygame.locals import *



class YannText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 220))
       
    def move(self):
        pass




pygame.init()

FramePerSec = pygame.time.Clock()

displays = pygame.display.set_mode((300,300))
displays.fill((255, 255, 255))

font = pygame.font.SysFont("Verdana", 20)
helloworld = font.render("helloworld", True, (0, 0, 0))

yt = YannText()
all_sprites = pygame.sprite.Group()
all_sprites.add(yt)

fini = False

x = 10
y = 10

#Game Loop
while True:

    displays.fill((255, 255, 255))

    displays.blit(helloworld, (x,y))
    x = x + 1
    y = y + 1

    for entity in all_sprites:
        displays.blit(entity.image, entity.rect)
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            fini = True

    if fini:
        break
    
    pygame.display.update()
    FramePerSec.tick(30)
