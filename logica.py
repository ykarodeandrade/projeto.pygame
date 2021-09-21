# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from constantes import Dados,Estado
#from assets import tela_inicial
from game_screen import game_screen
from init_screen import init_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((Dados.LARGURA, Dados.ALTURA))
pygame.display.set_caption('ESCAPING THE WELL')
state = Estado.STILL
while state != Estado.FALLING:
    if state == Estado.STILL:
        state = init_screen(window)
    elif state == Estado.JUMPING:
        state = game_screen(window)
    else:
        state = Estado.FALLING

game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados 