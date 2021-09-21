import pygame
import os
#from constantes import IMG_DIR,FNT_DIR,SND_DIR,LARGURA,ALTURA,BLOCO_ALTURA,BLOCO_LARGURA,DOG_ALTURA,DOG_LARGURA
from constantes import IMG_DIR,FNT_DIR,SND_DIR,Dados

pygame.init()

font = pygame.font.Font(os.path.join(FNT_DIR,'score.ttf'),48)
texto_inicial = font.render('ESCAPING THE WELL', True, (255, 0, 0))
texto_final = font.render('GAME OVER', True, (255, 0, 0))
background = pygame.image.load(os.path.join(IMG_DIR,'poço.png'))
background= pygame.transform.scale(background, (Dados.LARGURA, Dados.ALTURA))

agua=pygame.image.load(os.path.join(IMG_DIR,'water.png'))
agua=pygame.transform.scale(agua, (Dados.LARGURA, Dados.ALTURA-500))
bloco_img = pygame.image.load(os.path.join(IMG_DIR,'blocks.png'))
bloco_img = pygame.transform.scale(bloco_img, (Dados.BLOCO_LARGURA, Dados.BLOCO_ALTURA))
dog_img = pygame.image.load(os.path.join(IMG_DIR,'personagem.png'))
dog_img = pygame.transform.scale(dog_img, (Dados.DOG_LARGURA, Dados.DOG_ALTURA))
score_font=pygame.font.Font(os.path.join(FNT_DIR,'score.ttf'),28)
# Carrega os sons do jogo

pygame.mixer.music.load(os.path.join(SND_DIR,'geral.ogg'))
pygame.mixer.music.set_volume(0.4)
som_pulo = pygame.mixer.Sound(os.path.join(SND_DIR,'pulo.wav'))
som_gameover = pygame.mixer.Sound(os.path.join(SND_DIR,'GameOver.wav'))

# Recebe uma imagem de sprite sheet e retorna uma lista de imagens. 
# É necessário definir quantos sprites estão presentes em cada linha e coluna.
# Essa função assume que os sprites no sprite sheet possuem todos o mesmo tamanho.

def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

def blocos(x, y):
    lista_x=[x/2,x-100,x-200,x-400] 
    lista_y=[y-100,y-200,y-400,y-500]
    return lista_x,lista_y