
import pygame
from pygame.locals import *
from sys import exit
#Importa a funcao de escolher numeros inteiros aleatorios (radint) da biblioteca random
from random import randint

pygame.init()
largura = 640
altura = 480
x = largura / 2
y = altura / 2
#Cria novas variaveis de onde o quadrado amarelo iniciará, iniciando o quadrado em uma posicao aleatoria dentro da limitação de pixels indicados
x_amarelo = randint(40, 600)
y_amarelo = randint(40, 440)

pygame.display.set_caption("Primeiro jogo com Pygame")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                x = x - 5
            elif event.key == K_d or event.key == K_RIGHT:
                x = x + 5
            elif event.key == K_w or event.key == K_UP:
                y = y - 5
            elif event.key == K_s or event.key == K_DOWN:
                y = y + 5
        if event.type == QUIT:
            exit()
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x = x - 5
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x = x + 5
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y = y - 5
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y = y + 5
    #Atribui o quadrado verde e o amarelo dentro de variaveis para condicionar e continuar o processo
    quad_verde = pygame.draw.rect(tela, (144, 238, 144), (x, y, 50, 50))
    quad_amarelo = pygame.draw.rect(tela, (255, 255, 0), (x_amarelo, y_amarelo, 40, 40))
    #Se o quadrado verde colidir com o amarelo:
    if quad_verde.colliderect(quad_amarelo):
    #O quadrado reaparecerá em uma posicao diferente da inicial/anterior
        x_amarelo = randint(40, 600)
        y_amarelo = randint(50, 430)
    #Se o quadrado verde for menor do que a parte esquerda da tela que é = 0, logo ele saiu da tela, entao o programa é terminado/exit
                                                #ou
    #Se o quadrado verde mais a soma de seu tamanho (para garantir que a partir do momento da colisao, a condição acontecer) for maior que a largura, no caso a direta da tela, entao o programa é terminado
                                                #ou
    #Se o quadrado verde for menor que a parte de cima da tela, que é = 0, logo ele saiu da tela, entao o programa é terminado/exit
                                                #ou
    #Se o quadrado verde mais a soma de seu tamanho (para garantir que a partir do momento da colisao, a condicao acontecerá) for maior que a altura, no caso a parte de cima da tela, entao o programa é terminado
    if (x < 0 or x + 50 > largura) or (y < 0 or y + 50 > altura):
        exit()
    pygame.display.update()