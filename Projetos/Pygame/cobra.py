import pygame
from pygame.locals import *
from sys import exit
from random import randint
 
pygame.init()
largura = 640
altura = 480
tamanho_bloco = 30  # tamanho de cada "quadradinho" da cobra e da comida
 
pontos = 0
fonte = pygame.font.SysFont("arial", 20, bold=True)
fonte_gameover = pygame.font.SysFont("arial", 26, bold=True)
 
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
 
# A cobra é uma lista de posições (x, y). O primeiro item é a cabeça.
cobra = [(largura // 2, altura // 2)]
direcao = (tamanho_bloco, 0)       # direção atual do movimento
proxima_direcao = direcao          # direção escolhida pelo jogador, aplicada no próximo passo
 
def nova_posicao_azul(cobra):
    # Sorteia uma posição alinhada à grade que não esteja em cima da cobra
    while True:
        pos = (
            randint(0, (largura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco,
            randint(0, (altura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco,
        )
        if pos not in cobra:
            return pos
 
x_azul, y_azul = nova_posicao_azul(cobra)
 
morte = False
velocidade = 8  # quantos "passos" a cobra dá por segundo (aumente para deixar mais rápido)
 
while True:
    relogio.tick(velocidade)
    tela.fill((0, 0, 0))
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN and not morte:
            # A checagem "direcao != oposto" impede que a cobra vire 180° sobre si mesma
            if (event.key == K_a or event.key == K_LEFT) and direcao != (tamanho_bloco, 0):
                proxima_direcao = (-tamanho_bloco, 0)
            elif (event.key == K_d or event.key == K_RIGHT) and direcao != (-tamanho_bloco, 0):
                proxima_direcao = (tamanho_bloco, 0)
            elif (event.key == K_w or event.key == K_UP) and direcao != (0, tamanho_bloco):
                proxima_direcao = (0, -tamanho_bloco)
            elif (event.key == K_s or event.key == K_DOWN) and direcao != (0, -tamanho_bloco):
                proxima_direcao = (0, tamanho_bloco)
 
    if not morte:
        direcao = proxima_direcao
        cabeca_x, cabeca_y = cobra[0]
        nova_cabeca = (cabeca_x + direcao[0], cabeca_y + direcao[1])
 
        # Colisão com as bordas da tela
        if (nova_cabeca[0] < 0 or nova_cabeca[0] + tamanho_bloco > largura or
                nova_cabeca[1] < 0 or nova_cabeca[1] + tamanho_bloco > altura):
            morte = True
 
        # Colisão com o próprio corpo
        elif nova_cabeca in cobra:
            morte = True
 
        else:
            cobra.insert(0, nova_cabeca)  # adiciona a nova cabeça
 
            quad_cabeca = pygame.Rect(nova_cabeca[0], nova_cabeca[1], tamanho_bloco, tamanho_bloco)
            quad_azul = pygame.Rect(x_azul, y_azul, tamanho_bloco, tamanho_bloco)
 
            if quad_cabeca.colliderect(quad_azul):
                pontos += 1
                x_azul, y_azul = nova_posicao_azul(cobra)
                # Não remove o último segmento aqui -> a cobra cresce em 1 bloco
            else:
                cobra.pop()  # remove o último segmento -> mantém o tamanho ao só andar
 
    # Desenha a comida (quadrado azul)
    pygame.draw.rect(tela, (0, 0, 80), (x_azul, y_azul, tamanho_bloco, tamanho_bloco))
 
    # Desenha cada segmento da cobra
    for segmento in cobra:
        pygame.draw.rect(tela, (144, 238, 144), (segmento[0], segmento[1], tamanho_bloco, tamanho_bloco))
 
    # Pontuação
    texto_formatado = f"Pontuação: {pontos}"
    texto_renderizado = fonte.render(texto_formatado, True, (255, 255, 255))
    tela.blit(texto_renderizado, (3, 455))
 
    if morte:
        texto_fim = fonte_gameover.render("GAME OVER - Pressione R para reiniciar", True, (255, 0, 0))
        tela.blit(texto_fim, (largura // 2 - 220, altura // 2 - 13))
        keys = pygame.key.get_pressed()
        if keys[K_r]:
            cobra = [(largura // 2, altura // 2)]
            direcao = (tamanho_bloco, 0)
            proxima_direcao = direcao
            pontos = 0
            morte = False
            x_azul, y_azul = nova_posicao_azul(cobra)
 
    pygame.display.update()