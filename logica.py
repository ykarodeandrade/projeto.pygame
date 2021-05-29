# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from constantes import LARGURA, ALTURA,STILL,JUMPING,FALLING
#from assets import tela_inicial
from game_screen import game_screen
from init_screen import init_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('ESCAPING THE WELL')
state = STILL
while state != FALLING:
    if state == STILL:
        state = init_screen(window)
    elif state == JUMPING:
        state = game_screen(window)
    else:
        state = FALLING

game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados 