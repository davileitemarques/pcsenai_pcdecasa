#Importa as principais bibliotecas do Pygame
import pygame
from pygame.locals import *
from sys import exit
#Inicia o Pygame, introduz a variavel da altura e largura da tela, e o ponto inicial do objeto
pygame.init()
largura = 640
altura = 480
x = largura / 2
y = altura / 2
#Define o texto que aparecerá no topo da janela
pygame.display.set_caption("Primeiro jogo com Pygame")
#Define o framerate(FPS)do jogo
relogio = pygame.time.Clock()
#Cria a tela usando as variaveis de largura e altura criadas anteriormente
tela = pygame.display.set_mode((largura, altura))
#Loop principal pro funcionamento do jogo
while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
#Percorre a lista de todas as acoes feitas pelo usuario no frame atual
    for event in pygame.event.get():
#Verifica se o evento atual foi pressionar a tecla W ou S ou D ou A
        if event.type == KEYDOWN:
#Se pressionado A, o objeto move 5 pixels para esquerda (x - 5)
            if event.key == K_a or event.key == K_LEFT:
                x = x - 5
#Se pressionado D, o objeto move 5 pixels para a direita (x + 5)
            elif event.key == K_d or event.key == K_RIGHT:
                x = x + 5
#Se pressionado W, o objeto move 5 pixels para cima (y - 5)
            elif event.key == K_w or event.key == K_UP:
                y = y - 5
#Se pressionado S, o objeto move 5 pixels para baixo (y + 5)
            elif event.key == K_s or event.key == K_DOWN:
                y = y + 5
#Verifica se o usuario clicou no botao X da janela, se sim, a janela é fechada
        if event.type == QUIT:
            exit()
#Verifica se as teclas estao sendo seguradas, se sim, elas grdualmente continuam indo para as direcoes acionadas
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x = x - 5
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x = x + 5
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y = y - 5
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y = y + 5
#Desenha o objeto interativo (quadrado), sua posicao inicial, sua cor e seu tamanho
    pygame.draw.rect(tela, (144, 238, 144), (x, y, 50, 50))
#Atualiza sobre tudo o que foi desenhado dentro da janela
    pygame.display.update()