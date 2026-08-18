
import pygame
from pygame.locals import *
from sys import exit
# Importa a funcao de escolher numeros inteiros aleatorios (randint) da biblioteca random
from random import randint
 
pygame.init()
pygame.mixer.init()
largura = 640
altura = 480
tamanho_bloco = 30  # tamanho de cada "quadradinho" da cobra e da comida
pontos = 0

# Variavel criada pra atribuir a fonte e o tamanho da fonte usada pra marcar a pontuação
fonte = pygame.font.SysFont("arial", 20, bold=True)
# Variavel criada pra atribuir a fonte da tela de GAME OVER apos morrer
fonte_gameover = pygame.font.SysFont("arial", 26, bold=True)
# Variavel criada pra atribuir a fonte da tela de FIM DE JOGO apos alcancar 10 pontos
fonte_fim = pygame.font.SysFont("arial", 40, bold=True)
pygame.display.set_caption("Rayquaza vs Deoxys")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
fundo = pygame.image.load("fundo.png").convert()
musica = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
hit = pygame.mixer.Sound("hitsound.mp3")
hit.set_volume(0.5)
vencer = pygame.mixer.Sound("win.mp3")
vencer.set_volume(0.5)
gameover = pygame.mixer.Sound("game_over.mp3")
gameover.set_volume(0.5)
# A cobra é uma lista de posições (x, y). O primeiro item é a cabeça.
cobra = [(largura // 2, altura // 2)]
direcao = (0, 0)       # direção atual do movimento
proxima_direcao = direcao          # direção escolhida pelo jogador, aplicada no próximo passo
 
def nova_posicao_azul(cobra):
    # Sorteia uma posição alinhada à grade que não esteja em cima da cobra
    while True:
        posicao = randint(0, (largura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco,  randint(0, (altura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
        if posicao not in cobra:
            return posicao

x_azul, y_azul = nova_posicao_azul(cobra)
morte = False
velocidade = 9

while True:
    relogio.tick(velocidade)
    tela.fill((0, 0, 0))
    tela.blit(fundo, (0, 0))
    cabeca_x, cabeca_y = cobra[0]
    #Se o quadrado verde for menor do que a parte esquerda da tela que é = 0, logo ele saiu da tela, entao o programa entra no GAME OVER e é terminado
                                                    #ou
        #Se o quadrado verde mais a soma de seu tamanho (para garantir que a partir do momento da colisao, a condição acontecer) for maior que a largura, no caso a direta da tela, entao o programa entra no GAME OVER e é terminado
                                                    #ou
        #Se o quadrado verde for menor que a parte de cima da tela, que é = 0, logo ele saiu da tela, entao o programa entra no GAME OVER e é terminado
                                                    #ou
        #Se o quadrado verde mais a soma de seu tamanho (para garantir que a partir do momento da colisao, a condicao acontecerá) for maior que a altura, no caso a parte de cima da tela, entao o programa entra no GAME OVER e é terminado
    if (cabeca_x < 0 or cabeca_x + tamanho_bloco > largura) or (cabeca_y < 0 or cabeca_y + tamanho_bloco > altura) or morte:
        pygame.mixer.music.stop()
        gameover.play()
        while True:
            texto_fim = fonte_fim.render("GAME OVER", True, (255, 0, 0))
            tela.blit(texto_fim, (largura // 2 - 120, altura // 2 - 50))
            texto_formatado = f"Pontuação: {pontos}"
            texto_renderizado = fonte_gameover.render(texto_formatado, True, (255, 255, 0))
            tela.blit(texto_renderizado, (largura // 2 - 87, altura // 2 - 13))
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()           


    # Condição de VITÓRIA (Fim do jogo ao alcançar 10 pontos)
    if pontos >= 10:
        pygame.mixer.music.stop()
        vencer.play()

        while True:
            texto_fim = fonte_fim.render("VENCEDOR!", True, (255, 0, 0))
            tela.blit(texto_fim, (largura // 2 - 100 ,  altura // 2 - 40))
            pygame.mixer.music.stop()
            vencer.play()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    proxima_direcao = (0, 0)
    teclas = pygame.key.get_pressed()
            # A checagem "direcao != oposto" impede que a cobra vire 180° sobre si mesma
    if (teclas[K_a] or teclas[K_LEFT]) and direcao != (tamanho_bloco, 0):
        proxima_direcao = (-tamanho_bloco, 0)
    elif (teclas[K_d] or teclas[K_RIGHT]) and direcao != (-tamanho_bloco, 0):
        proxima_direcao = (tamanho_bloco, 0)
    elif (teclas[K_w] or teclas[K_UP]) and direcao != (0, tamanho_bloco):
        proxima_direcao = (0, -tamanho_bloco)
    elif (teclas[K_s] or teclas[K_DOWN]) and direcao != (0, -tamanho_bloco):
        proxima_direcao = (0, tamanho_bloco)

    # Atualiza a movimentação da cobra
    direcao = proxima_direcao
    nova_cabeca = (cabeca_x + direcao[0], cabeca_y + direcao[1])
    
    if direcao != (0, 0):
        if nova_cabeca in cobra:
            morte = True
        else:
            cobra.insert(0, nova_cabeca)  # adiciona a nova cabeça
            quad_cabeca = pygame.Rect(nova_cabeca[0], nova_cabeca[1], tamanho_bloco, tamanho_bloco)
            quad_azul = pygame.Rect(x_azul, y_azul, tamanho_bloco, tamanho_bloco)
            
            if quad_cabeca.colliderect(quad_azul):
                hit.play()
                pontos += 1
                x_azul, y_azul = nova_posicao_azul(cobra)
            else:
                cobra.pop()

    # Desenha a comida (quadrado vermelho)
    pygame.draw.rect(tela, (255, 0, 0), (x_azul, y_azul, 30, 30))
    
    # Desenha cada segmento da cobra
    for segmento in cobra:
        pygame.draw.rect(tela, (144, 238, 144), (segmento[0], segmento[1], tamanho_bloco, tamanho_bloco))
        
    # Pontuação na tela ativa
    texto_formatado = f"Pontuação: {pontos}"
    texto_renderizado = fonte.render(texto_formatado, True, (255, 255, 255))
    tela.blit(texto_renderizado, (3, 455))

    pygame.display.update()