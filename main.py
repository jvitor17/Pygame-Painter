#PygamePainter
import pygame
from pygame.locals import *
icon = pygame.image.load('icon.png')
pygame.init()

#Booleans
game_over = False
large = False

#Colors
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
cyan = (0,255,255)

white = (255,255,255)
brush_color = black
background_color = white

#Mouse position on screen
x, y = 0, 0

#Size of brush
brush_size = 1

#Surfaces
screen = pygame.display.set_mode((800,600), RESIZABLE)
canvas = pygame.Surface((2000,2000), pygame.SRCALPHA, 32)
canvas.convert_alpha()

pygame.display.set_caption("PygamePainter")
pygame.display.set_icon(icon)

while not game_over:

    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True

        #Keyboard pressed key event handler
        if event.type == KEYDOWN:
            #Change colors with numpad
            if event.key == K_1:
                brush_color = red
            if event.key == K_2:
                brush_color = green
            if event.key == K_3:
                brush_color = blue
            if event.key == K_4:
                brush_color = cyan
            if event.key == K_5:
                brush_color = magenta
            if event.key == K_6:
                brush_color = yellow
            if event.key == K_7:
                brush_color = black
            if event.key == K_8:
                brush_color = white

            if event.key == K_x:
                background_color = brush_color

            #Control brush size with UP and DOWN arrow keys
            if event.key == K_DOWN:
                brush_size -= 1
                if brush_size < 1:
                    brush_size = 1
            if event.key == K_UP:
                brush_size += 1
                if brush_size > 60:
                    brush_size = 60

            #Save image to a file
            if event.key == K_s:
                pygame.image.save(screen,'desenho.png')

    #Updates x and y with mouse pos on screen a thousand times per second
    x, y = pygame.mouse.get_pos()


    #Handle mouse left click to draw on screen
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(canvas,(brush_color),(x,y),brush_size,0)

    screen.fill(background_color)
    screen.blit(canvas,(0,0))
    pygame.display.update()

pygame.quit()
