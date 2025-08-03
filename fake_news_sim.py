import pygame
import numpy as np
import random

# Parâmetros
grid_size = 80
cell_size = 10
width = grid_size * cell_size
height = grid_size * cell_size
fps = 6

# Parâmetros de propagação
prob_share = 0.6
resistance_rate = 0.1
threshold = 1 # número de vizinhos necessários para compartilhar
initial_infected = 10
delay_max = 3

# Influencers
influencer_count = 120
influencer_positions = []
influencer_break_resistance_chance = 0.7

# Cores
colors = {
    0: (220, 220, 220),  # não ouviu
    1: (30, 144, 255),   # compartilhou
    2: (220, 50, 50),    # recusou
    10: (255, 215, 0)    # influencer que ainda não compartilhou (amarelo claro)
}

# Inicialização
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fake News com Influencers Reais")
clock = pygame.time.Clock()

# Grade de estados
grid = np.zeros((grid_size, grid_size), dtype=int)
delay_grid = np.random.randint(0, delay_max + 1, size=(grid_size, grid_size))

# Define resistentes
resistants = np.random.rand(grid_size, grid_size) < resistance_rate
grid[resistants] = 2

# Define posições dos influencers (marcados visualmente mas começam como estado 0)
for _ in range(influencer_count):
    while True:
        i, j = np.random.randint(0, grid_size), np.random.randint(0, grid_size)
        if grid[i, j] == 0:
            influencer_positions.append((i, j))
            break

# Define as pessoas que começam compartilhando (fake news seeds)
for _ in range(initial_infected):
    while True:
        i, j = np.random.randint(0, grid_size), np.random.randint(0, grid_size)
        if grid[i, j] == 0 and (i, j) not in influencer_positions:
            grid[i, j] = 1
            break

def draw_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            if (i, j) in influencer_positions and grid[i, j] != 1:
                color = colors[10]  # influencer ainda não compartilhou
            else:
                color = colors.get(grid[i, j], (0, 0, 0))  # fallback para preto
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

def is_influencer(i, j):
    return (i, j) in influencer_positions

def count_sharing_neighbors(i, j):
    count = 0
    influencer_nearby = False
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + dx, j + dy
        if 0 <= ni < grid_size and 0 <= nj < grid_size:
            if grid[ni, nj] == 1:
                count += 1
                if is_influencer(ni, nj):
                    count += 1  # influencer vale por 2
                    influencer_nearby = True
    return count, influencer_nearby

# Loop principal
running = True
paused = False

while running:
    screen.fill((255, 255, 255))
    draw_grid()
    pygame.display.flip()

    if not paused:
        new_grid = grid.copy()
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i, j] == 0:
                    if delay_grid[i, j] > 0:
                        delay_grid[i, j] -= 1
                        continue
                    neighbors, influencer_nearby = count_sharing_neighbors(i, j)
                    if neighbors >= threshold:
                        chance = prob_share
                        if is_influencer(i, j):  # se a célula é um influencer
                            chance += 0.2  # influencers são mais suscetíveis
                        if random.random() < chance:
                            new_grid[i, j] = 1
                        else:
                            new_grid[i, j] = 2
                elif grid[i, j] == 2:  # resistente
                    _, influencer_nearby = count_sharing_neighbors(i, j)
                    if influencer_nearby:
                        if random.random() < influencer_break_resistance_chance:
                            new_grid[i, j] = 1
        grid = new_grid

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    clock.tick(fps)

pygame.quit()
