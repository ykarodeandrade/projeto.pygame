# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 500
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

# ----- Inicia assets
BLOCO_WIDTH = 85
BLOCO_HEIGTH = 38
DOG_WIDTH = 80
DOG_HEIGTH = 80
font = pygame.font.SysFont('Algerian', 48)
text1 = font.render('SABRINA EU TE AMO', True, (255, 0, 0))
background = pygame.image.load('img/Background.png').convert_alpha()
background= pygame.transform.scale(background, (WIDTH, HEIGHT))
bloco_img = pygame.image.load('img/blocks.png').convert_alpha()
bloco_img = pygame.transform.scale(bloco_img, (BLOCO_WIDTH, BLOCO_HEIGTH))
dog_img = pygame.image.load('img/dogremove.png').convert_alpha()
dog_img = pygame.transform.scale(dog_img, (DOG_WIDTH, DOG_HEIGTH))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Ship(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
class Bloco(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-BLOCO_WIDTH)
        self.rect.y = random.randint(-100, -BLOCO_HEIGTH)
        self.speedx = self.rect.x #random.randint(-3, 3)
        self.speedy = 2

    def update(self):
        # Atualizando a posição do Blocoo
        #self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o Blocoo passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-BLOCO_WIDTH)
            self.rect.y = random.randint(-100, -BLOCO_HEIGTH)
            #self.speedx = random.randint(-3, 3)
            self.speedy = 2 #random.randint(2, 9)

game = True
#bloco_x = random.randint(0, WIDTH-BLOCO_WIDTH)
# y negativo significa que está acima do topo da janela. O Blocoo começa fora da janela
# bloco_y = random.randint(-100, -BLOCO_HEIGTH)
background_x=0
background_y=0
# background_y2=-600
# background_speedx=0
# background_speedy=1
# bloco_speedx = bloco_x
# bloco_speedy = 2
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
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8
    todos_sprites.update()
    # ----- Atualiza estado do jogo
    # Atualizando a posição do Blocoo
    #bloco_x += bloco_speedx
    #bloco_y += bloco_speedy
    # background_x+=background_speedx
    # background_y+=background_speedy
    # background_y2+=background_speedy
    # Se o Blocoo passar do final da tela, volta para cima
    # if bloco_y > HEIGHT or bloco_x + BLOCO_WIDTH < 0 or bloco_x > WIDTH:
    #     #bloco_x = random.randint(0, WIDTH-BLOCO_WIDTH)
    #     bloco_y = random.randint(-100, -BLOCO_HEIGTH)
    # elif background_y > HEIGHT or background_x + BLOCO_WIDTH < 0 or background_x > WIDTH:
    #     background_x = 0
    #     background_y = 0
    #     background_y2=-600
    # bloco1.update()
    # bloco2.update()
    # bloco3.update()
    # bloco4.update()
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (background_x, background_y))
    todos_sprites.draw(window)
    #window.blit(background, (background_x, background_y2))
    #window.blit(text1, (16, 250))
    #window.blit(bloco_img, (bloco_x, bloco_y))
    # window.blit(bloco1.image, bloco1.rect)
    # window.blit(bloco2.image, bloco2.rect)
    # window.blit(bloco3.image, bloco3.rect)
    # window.blit(bloco4.image, bloco4.rect)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
