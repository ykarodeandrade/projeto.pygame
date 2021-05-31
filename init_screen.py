import pygame
import random
from os import path
from constantes import ALTURA, IMG_DIR, GREEN, FPS, JUMPING, FALLING, LARGURA


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'ceu.png')).convert()
    background=pygame.transform.scale(background, (LARGURA, ALTURA-130))
    arvore=pygame.image.load(path.join(IMG_DIR, 'tree.png')).convert()
    font = pygame.font.SysFont('Algerian', 48)
    texto_inicial = font.render('ESCAPING THE WELL', True, (0, 0, 0))
    background_rect = background.get_rect()
    arvore_rect= arvore.get_rect()
    poco_inicio= pygame.image.load(path.join(IMG_DIR, 'poço_certo2.png')).convert()
    poco_inicio=pygame.transform.scale(poco_inicio, (100, 80))
    personagem=pygame.image.load(path.join(IMG_DIR, 'personagem_só.png')).convert()
    personagem=pygame.transform.scale(personagem, (80, 80))
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = JUMPING
                running = False

            if event.type == pygame.KEYUP:
                state = FALLING
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(GREEN)
        screen.blit(background, background_rect)
        screen.blit(arvore, (10, ALTURA-305))
        screen.blit(poco_inicio, (320, ALTURA-100))
        screen.blit(texto_inicial,(20,20))
        screen.blit(personagem, (200, ALTURA-110))


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state