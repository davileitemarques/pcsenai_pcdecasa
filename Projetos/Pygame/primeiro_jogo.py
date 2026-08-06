import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()
    pygame.draw.rect(tela, (255, 0, 0), (260, 345, 40, 50))
    pygame.draw.circle(tela, (0, 255, 0), (350, 354), 40)
    pygame.draw.line(tela, (255, 255, 0), (0, 400), (960, 400), 20)