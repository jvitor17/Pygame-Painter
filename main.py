import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


    if event.type ==KEYDOWN:
        if event.key == K_UP:
            pygame.image.save(screen,'desenho.png')


    pos = pygame.mouse.get_pos()
    
    if pygame.mouse.get_pressed()[0]:
        screen.set_at(pos,(0,0,0))

    pygame.display.update()
        

