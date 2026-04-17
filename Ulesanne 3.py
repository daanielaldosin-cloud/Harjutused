import pygame
import sys

pygame.init()

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Harjutamine")


def draw_grid(surface, cell_size, rows, cols, color):
    for row in range(rows + 1):
        y = row * cell_size
        pygame.draw.line(surface, color, (0, y), (cols * cell_size, y))

    for col in range(cols + 1):
        x = col * cell_size
        pygame.draw.line(surface, color, (x, 0), (x, rows * cell_size))


cell_size = 20
rows = HEIGHT // cell_size
cols = WIDTH // cell_size
line_color = (255, 0, 0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((180, 255, 180))

    draw_grid(screen, cell_size, rows, cols, line_color)

    pygame.display.flip()

pygame.quit()
sys.exit()