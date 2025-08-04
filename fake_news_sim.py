import pygame
import numpy as np
import random

class FakeNewsSimulation:
    def __init__(self, grid_size=80, cell_size=10, fps=6,
                 prob_share=0.6, resistance_rate=0.1, threshold=1,
                 initial_infected=10, delay_max=3, influencer_count=400,
                 influencer_break_resistance_chance=0.7, visualizar=True):

        # Parâmetros principais
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.width = grid_size * cell_size
        self.height = grid_size * cell_size
        self.fps = fps
        self.prob_share = prob_share
        self.resistance_rate = resistance_rate
        self.threshold = threshold
        self.initial_infected = initial_infected
        self.delay_max = delay_max
        self.influencer_count = influencer_count
        self.influencer_break_resistance_chance = influencer_break_resistance_chance
        self.visualizar = visualizar
        if self.visualizar:
            pygame.init()
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("Fake News com Influencers Reais")
            self.clock = pygame.time.Clock()
        # Estados
        self.colors = {
            0: (220, 220, 220),
            1: (30, 144, 255),
            2: (220, 50, 50),
            10: (255, 215, 0)
        }

        self.influencer_positions = []

        # Inicialização
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fake News com Influencers Reais")
        self.clock = pygame.time.Clock()

        # Grade
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.delay_grid = np.random.randint(0, delay_max + 1, size=(grid_size, grid_size))

        # Estatísticas
        self.step = 0
        self.stats = {
            "step": [],
            "shared": [],
            "resisted": [],
            "unaware": []
        }

        self._initialize_grid()

    def _initialize_grid(self):
        resistants = np.random.rand(self.grid_size, self.grid_size) < self.resistance_rate
        self.grid[resistants] = 2

        for _ in range(self.influencer_count):
            while True:
                i, j = np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)
                if self.grid[i, j] == 0:
                    self.influencer_positions.append((i, j))
                    break

        for _ in range(self.initial_infected):
            while True:
                i, j = np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)
                if self.grid[i, j] == 0 and (i, j) not in self.influencer_positions:
                    self.grid[i, j] = 1
                    break

    def is_influencer(self, i, j):
        return (i, j) in self.influencer_positions

    def count_sharing_neighbors(self, i, j):
        count = 0
        influencer_nearby = False
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < self.grid_size and 0 <= nj < self.grid_size:
                if self.grid[ni, nj] == 1:
                    count += 1
                    if self.is_influencer(ni, nj):
                        count += 1
                        influencer_nearby = True
        return count, influencer_nearby

    def update(self):
        new_grid = self.grid.copy()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i, j] == 0:
                    if self.delay_grid[i, j] > 0:
                        self.delay_grid[i, j] -= 1
                        continue
                    neighbors, influencer_nearby = self.count_sharing_neighbors(i, j)
                    if neighbors >= self.threshold:
                        chance = self.prob_share
                        if self.is_influencer(i, j):
                            chance += 0.2
                        new_grid[i, j] = 1 if random.random() < chance else 2
                elif self.grid[i, j] == 2:
                    _, influencer_nearby = self.count_sharing_neighbors(i, j)
                    if influencer_nearby:
                        if random.random() < self.influencer_break_resistance_chance:
                            new_grid[i, j] = 1
        self.grid = new_grid
        self._collect_stats()
        self.step += 1

    def _collect_stats(self):
        self.stats["step"].append(self.step)
        self.stats["shared"].append(np.sum(self.grid == 1))
        self.stats["resisted"].append(np.sum(self.grid == 2))
        self.stats["unaware"].append(np.sum(self.grid == 0))

    def draw(self):
        self.screen.fill((255, 255, 255))
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) in self.influencer_positions and self.grid[i, j] != 1:
                    color = self.colors[10]
                else:
                    color = self.colors.get(self.grid[i, j], (0, 0, 0))
                pygame.draw.rect(self.screen, color,
                                 (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self, max_steps=100):
        running = True
        paused = False

        while running and self.step < max_steps:
            if self.visualizar:
                self.draw()

            if not paused:
                self.update()

            if self.visualizar:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            paused = not paused
            else:
                # No modo silencioso (sem pygame), apenas avança
                running = True

            if self.visualizar:
                self.clock.tick(self.fps)

        if self.visualizar:
            pygame.quit()


    def get_stats(self):
        return self.stats
