from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')
SND_DIR = path.join(path.dirname(__file__), 'snd')
FNT_DIR = path.join(path.dirname(__file__),'font')

class Dados:
    # Constantes relacionadas ao jogo
    LARGURA = 500
    ALTURA = 600
    FPS = 50
    GRAVITY = 2
    # Constantes relacionadas a tamanhos
    BLOCO_LARGURA = 85
    BLOCO_ALTURA = 38
    DOG_LARGURA = 180
    DOG_ALTURA = 180
    # Define a altura do chão
    GROUND = ALTURA * 5 // 6
    
class Estado:
    # Define estados possíveis do jogador
    STILL = 0            #constante
    JUMPING = 1          #pulando
    FALLING = 2          #caindo
    WALKING_RIGTH = 3    #andando para direita
    WALKING_LEFT = 4     #andando para esquerda
    # Define a velocidade inicial no pulo
    JUMP_SIZE = 30

class Cor:
    # Define algumas variáveis com as cores básicas
    WHITE = (255, 255, 255)
    GREEN = (0, 128, 0)
    BLACK = (0, 0, 0)
