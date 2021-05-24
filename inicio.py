# Ricardo, Rodrigo e Ykaro
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
LARGURA = 500
ALTURA = 600
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('WATER JUMP')

# ----- Inicia assets
BLOCO_LARGURA = 85
BLOCO_ALTURA = 38
DOG_LARGURA = 80
DOG_ALTURA = 80
font = pygame.font.SysFont('Algerian', 48)
text1 = font.render('TESTANDO', True, (255, 0, 0))
background = pygame.image.load('img/Background.png').convert_alpha()
background= pygame.transform.scale(background, (LARGURA, ALTURA))
bloco_img = pygame.image.load('img/blocks.png').convert_alpha()
bloco_img = pygame.transform.scale(bloco_img, (BLOCO_LARGURA, BLOCO_ALTURA))
dog_img = pygame.image.load('img/dogremove.png').convert_alpha()
dog_img = pygame.transform.scale(dog_img, (DOG_LARGURA, DOG_ALTURA))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Ship(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA
        self.speedx = 0
        self.speedy = 0
        #self.rect.y=ALTURA-DOG_ALTURA
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > LARGURA: #DIREITA
            self.rect.right = LARGURA  
        if self.rect.left < 0: #ESQUERDA
            self.rect.left = 0
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
            self.speedy=0
class Bloco(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA-BLOCO_LARGURA)
        self.rect.y = random.randint(-100, -BLOCO_ALTURA)
        self.speedx = self.rect.x #random.randint(-3, 3)
        self.speedy = 2

    def update(self):
        # Atualizando a posição do Blocoo
        #self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o Blocoo passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            self.rect.x = random.randint(0, LARGURA-BLOCO_LARGURA)
            self.rect.y = random.randint(-100, -BLOCO_ALTURA)
            #self.speedx = random.randint(-3, 3)
            self.speedy = 2 #random.randint(2, 9)

game = True
background_x=0
background_y=0
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 50
# Criando um grupo de meteoros
todos_sprites = pygame.sprite.Group()
# Criando o jogador
player = Ship(dog_img)
todos_sprites.add(player)
# Criando os meteoros
for i in range(8):
    bloco = Bloco(bloco_img)
    todos_sprites.add(bloco)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            if event.key == pygame.K_SPACE:
                player.speedy += -8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8
            if event.key == pygame.K_SPACE:
                player.speedy += 16
    todos_sprites.update()
    # ----- Atualiza estado do jogo
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (background_x, background_y))
    todos_sprites.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
