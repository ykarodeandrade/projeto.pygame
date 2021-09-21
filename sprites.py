import pygame
import random
from constantes import Estado
from assets import *

pygame.init()
pygame.mixer.init()


# ----- Inicia estruturas de dados
# Definindo os novos tipos




class Ship(pygame.sprite.Sprite):
    def __init__(self, img, blocos, som_pulo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Define sequências de sprites de cada animação    
        spritesheet = load_spritesheet(img, 4, 4)
        self.animations = {
            Estado.STILL: spritesheet[0:4],                #constante
            Estado.WALKING_RIGTH: spritesheet[4:8],        #andando      
            Estado.WALKING_LEFT:  spritesheet[8:12],
            Estado.JUMPING: spritesheet[0:1],              #pulando
            Estado.FALLING: spritesheet[0:1],
        }
        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.animacao = Estado.STILL
        self.state = Estado.STILL
        # Define animação atual
        self.animation = self.animations[self.animacao]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        #self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = Dados.LARGURA / 2
        self.rect.bottom = Dados.LARGURA - (100 + Dados.BLOCO_ALTURA)
        self.speedx = 0
        self.speedy = 0
        self.platforms = blocos
        self.highest_y = self.rect.bottom
        self.som_pulo = som_pulo
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 300
        self.score=0
        self.ultimo=0
        
        
        
    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.animacao]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center
        # Vamos tratar os movimentos de maneira independente.
        # Primeiro tentamos andar no eixo y e depois no x.
        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += Dados.GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = Estado.FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy

        # Atualiza altura no mapa
        if self.state != Estado.FALLING:
            self.highest_y = self.rect.bottom

        # Se colidiu com algum bloco, volta para o ponto antes da colisão
    

        # Tratamento especial para plataformas
        # Plataformas devem ser transponíveis quando o personagem está pulando
        # mas devem pará-lo quando ele está caindo. Para pará-lo é necessário que
        # o jogador tenha passado daquela altura durante o último pulo.
        
        if self.speedy > 0:  # Está indo para baixo
            collisions = pygame.sprite.spritecollide(self, self.platforms, False)
            # Para cada tile de plataforma que colidiu com o personagem
            # verifica se ele estava aproximadamente na parte de cima
            for platform in collisions:
                # Verifica se a altura alcançada durante o pulo está acima da
                # plataforma.
                if self.highest_y <= platform.rect.top:
                    bloco_atual=platform.id
                    if bloco_atual!=self.ultimo:
                        self.score+=100
                        self.ultimo=bloco_atual
                    self.rect.bottom = platform.rect.top
                    # Atualiza a altura no mapa
                    self.highest_y = self.rect.bottom
                    # Para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = Estado.STILL
                    
        
        

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= Dados.LARGURA:
            self.rect.right = Dados.LARGURA
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        # O personagem não colide com as plataformas quando está andando na horizontal
        
    # Método que faz o personagem pular (extraído de: https://github.com/Insper/pygame-snippets/blob/master/jump.py)
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == Estado.STILL:
            self.speedy -= Estado.JUMP_SIZE
            self.state = Estado.JUMPING 
        self.som_pulo.play()

class Bloco(pygame.sprite.Sprite):
    def __init__(self, img, x, y,id):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y 
        self.speedx = self.rect.x
        self.speedy = 1
        self.id = id
        self.inicio = x
    def update(self):
        # Atualizando a posição do Bloco
        if self.id==4:
            self.rect.x+=self.speedx
            if self.rect.x>self.inicio+40:#BLOCO_LARGURA:
                self.speedx=-1
            if self.rect.x<self.inicio-40:#BLOCO_LARGURA:
                self.speedx=1  
        self.rect.y += self.speedy
        # Se o Blocoo passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.bottom > Dados.ALTURA:
            self.rect.y =  -2