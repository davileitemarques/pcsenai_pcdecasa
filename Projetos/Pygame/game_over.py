
import pygame
from pygame.locals import *
from sys import exit
#Importa a funcao de escolher numeros inteiros aleatorios (randint) da biblioteca random
from random import randint

pygame.init()
largura = 640
altura = 480
x = largura / 2
y = altura / 2
#Cria novas variaveis de onde o quadrado amarelo iniciará, iniciando o quadrado em uma posicao aleatoria dentro da limitação de pixels indicados
x_azul = randint(40, 600)
y_azul = randint(40, 440)
pontos = 0
#Variavel criada pra atribuir a fonte e o tamanho da fonte usada pra marcar a pontuação
fonte = pygame.font.SysFont("arial", 20, bold=True)
#Variavel criada pra atribuir a fonte da tela de FIM DE JOGO apos alcancar 10 pontos
fonte_fim = pygame.font.SysFont("arial", 40, bold=True)
#Variavel criada pra atribuir a fonte da tela de GAME OVER apos morrer
fonte_gameover = pygame.font.SysFont("arial", 26, bold=True)
game_over = False
morte = False

pygame.display.set_caption("Primeiro jogo com Pygame")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    #Se o quadrado verde for menor do que a parte esquerda da tela que é = 0, logo ele saiu da tela, entao o programa entra no GAME OVER e é terminado
                                                #ou
    #Se o quadrado verde mais a soma de seu tamanho (para garantir que a partir do momento da colisao, a condição acontecer) for maior que a largura, no caso a direta da tela, entao o programa entra no GAME OVER e é terminado
                                                #ou
    #Se o quadrado verde for menor que a parte de cima da tela, que é = 0, logo ele saiu da tela, entao o programa entra no GAME OVER e é terminado
                                                #ou
    #Se o quadrado verde mais a soma de seu tamanho (para garantir que a partir do momento da colisao, a condicao acontecerá) for maior que a altura, no caso a parte de cima da tela, entao o programa entra no GAME OVER e é terminado
    if (x < 0 or x + 50 > largura) or (y < 0 or y + 50 > altura):
        morte = True
        texto_fim = fonte_fim.render("GAME OVER", True, (255, 0, 0))
        tela.blit(texto_fim, (largura // 2 - 120, altura // 2 - 50))
        #Parte exlusiva pra pontuacao e pra congelar a tela do jogo e so aparecer a pontuacao final e o game over
        texto_renderizado = fonte_gameover.render(texto_formatado, True, (255, 255, 0))
        tela.blit(texto_renderizado, (largura // 2 - 87, altura // 2 - 13))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()           
        pygame.display.update()
        continue
    if pontos >= 10:
        game_over = True
        texto_fim = fonte_fim.render("FIM DO JOGO!", True, (255, 0, 0))
        tela.blit(texto_fim, (largura // 2 - 150 ,  altura // 2 - 40))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pygame.display.update()
        continue
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
    quad_azul = pygame.draw.rect(tela, (0, 0, 80), (x_azul, y_azul, 37, 37))
    #Se o quadrado verde colidir com o amarelo:
    if quad_verde.colliderect(quad_azul):
    #O quadrado reaparecerá em uma posicao diferente da inicial/anterior
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
    texto_formatado = f"Pontuação: {pontos}"
    texto_renderizado = fonte.render(texto_formatado, True, (255, 255, 255))
    tela.blit(texto_renderizado, (3, 455))

    pygame.display.update()