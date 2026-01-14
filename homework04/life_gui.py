import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.width = life.cols * cell_size
        self.height = life.rows * cell_size
        self.screen_size = (self.width, self.height)
        self.cell_width = life.cols
        self.cell_height = life.rows
        self.paused = False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        current_grid = self.life.curr_generation
        for x in range(self.cell_height):
            for y in range(self.cell_width):
                coord_x = x * self.cell_size
                coord_y = y * self.cell_size
                color = pygame.Color("green") if current_grid[x][y] == 1 else pygame.Color("white")
                pygame.draw.rect(self.screen, color, (coord_x, coord_y, self.cell_size, self.cell_size))

    def run(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Game of Life")
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 24)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.paused = not self.paused
                elif event.type == MOUSEBUTTONDOWN and self.paused:
                    if event.button == 1:
                        x, y = event.pos
                        cell_x = x // self.cell_size
                        cell_y = y // self.cell_size
                        if 0 <= cell_x < len(self.life.curr_generation) and 0 <= cell_y < len(
                            self.life.curr_generation[0]
                        ):
                            current_state = self.life.curr_generation[cell_x][cell_y]
                            self.life.curr_generation[cell_x][cell_y] = 1 if current_state == 0 else 0
            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()
            text = font.render(f"Generation: {self.life.generations}", True, pygame.Color("black"))
            self.screen.blit(text, (10, 10))
            pygame.display.flip()
            if not self.paused:
                self.life.step()
            clock.tick(self.speed)
        pygame.quit()
