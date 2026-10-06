import pygame
import random
import sys

# 1. Inicialização do Pygame
pygame.init()

# 2. Configurações da Tela e Cores
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Primeiro Jogo em Pygame")

COR_FUNDO = (30, 30, 30)      # Cinza escuro
COR_JOGADOR = (0, 255, 128)   # Verde
COR_COMIDA = (255, 50, 50)    # Vermelho
COR_TEXTO = (255, 255, 255)   # Branco

# 3. Variáveis do Jogador
tamanho_jogador = 40
jogador_x = LARGURA // 2
jogador_y = ALTURA // 2
velocidade = 5

# 4. Variáveis da Comida
tamanho_comida = 20
comida_x = random.randint(0, LARGURA - tamanho_comida)
comida_y = random.randint(0, ALTURA - tamanho_comida)

# 5. Pontuação e Fonte
pontos = 0
fonte = pygame.font.SysFont("Arial", 28)

# Controlar a taxa de quadros (FPS)
relogio = pygame.time.Clock()

# 6. Loop Principal do Jogo
rodando = True
while rodando:
    # --- A. Processamento de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # --- B. Leitura dos Controles (Movimentação Continuada) ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= velocidade
    if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - tamanho_jogador:
        jogador_x += velocidade
    if teclas[pygame.K_UP] and jogador_y > 0:
        jogador_y -= velocidade
    if teclas[pygame.K_DOWN] and jogador_y < ALTURA - tamanho_jogador:
        jogador_y += velocidade

    # --- C. Detecção de Colisão (Jogador vs Comida) ---
    rect_jogador = pygame.Rect(jogador_x, jogador_y, tamanho_jogador, tamanho_jogador)
    rect_comida = pygame.Rect(comida_x, comida_y, tamanho_comida, tamanho_comida)

    if rect_jogador.colliderect(rect_comida):
        pontos += 1
        # Repocisiona a comida em um local aleatório
        comida_x = random.randint(0, LARGURA - tamanho_comida)
        comida_y = random.randint(0, ALTURA - tamanho_comida)

    # --- D. Desenho na Tela ---
    tela.fill(COR_FUNDO) # Limpa a tela a cada quadro

    # Desenha o jogador e a comida
    pygame.draw.rect(tela, COR_JOGADOR, rect_jogador)
    pygame.draw.rect(tela, COR_COMIDA, rect_comida)

    # Renderiza o texto do placar
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, COR_TEXTO)
    tela.blit(texto_pontos, (10, 10))

    # --- E. Atualização da Tela ---
    pygame.display.flip()

    # Limita o jogo a 60 quadros por segundo (FPS)
    relogio.tick(60)

# Finaliza o Pygame ao sair do loop
pygame.quit()
sys.exit()