# import pygame
# import random
# from os import path
# from constantes import *

import pygame
import random
from os import path
from constantes import Dados, Cor, IMG_DIR,Estado, FNT_DIR
from assets import texto_inicial

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'ceu.png')).convert()
    background=pygame.transform.scale(background, (Dados.LARGURA, Dados.ALTURA-130))
    arvore=pygame.image.load(path.join(IMG_DIR, 'tree.png')).convert()
    font = pygame.font.Font(path.join(FNT_DIR,'score.ttf'),28)#('Algerian', 48)
    font2 = pygame.font.Font(path.join(FNT_DIR,'score.ttf'),18)
    texto_inicial = font.render('ESCAPING THE WELL', True, (0, 0, 0))
    background_rect = background.get_rect()
    arvore_rect= arvore.get_rect()
    poco_inicio= pygame.image.load(path.join(IMG_DIR, 'poço_certo2.png')).convert()
    poco_inicio=pygame.transform.scale(poco_inicio, (100, 80))
    personagem=pygame.image.load(path.join(IMG_DIR, 'personagem_só.png')).convert()
    personagem=pygame.transform.scale(personagem, (80, 80))
    direita=pygame.image.load(path.join(IMG_DIR, 'right.png')).convert()
    texto_direita = font2.render('right', True, (0, 0, 0))
    esquerda=pygame.image.load(path.join(IMG_DIR, 'left.png')).convert()
    texto_esquerda = font2.render('left', True, (0, 0, 0))
    espaço=pygame.image.load(path.join(IMG_DIR, 'jump.png')).convert()
    texto_espaço = font2.render('jump', True, (0, 0, 0))
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(Dados.FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = Estado.JUMPING
                running = False

            if event.type == pygame.KEYUP:
                state = Estado.FALLING
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Cor.GREEN)
        screen.blit(background, background_rect)
        screen.blit(arvore, (10, Dados.ALTURA-305))
        screen.blit(poco_inicio, (320, Dados.ALTURA-100))
        screen.blit(texto_inicial,(20,20))
        screen.blit(personagem, (200, Dados.ALTURA-110))
        screen.blit(direita, (150, Dados.ALTURA-500))
        screen.blit(texto_direita,(300,Dados.ALTURA-500))
        screen.blit(esquerda, (150, Dados.ALTURA-450))
        screen.blit(texto_esquerda,(300,Dados.ALTURA-450))
        screen.blit(espaço, (50, Dados.ALTURA-400))
        screen.blit(texto_espaço,(300,Dados.ALTURA-400))


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state