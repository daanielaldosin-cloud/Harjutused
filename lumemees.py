import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees")

pygame.draw.circle(screen, [255, 255, 255], [150, 230], 50, 0)

pygame.draw.circle(screen, [255, 255, 255], [150, 145], 40, 0)

pygame.draw.circle(screen, [255, 255, 255], [150, 80], 30, 0)

pygame.draw.circle(screen, [0, 0, 0], [160, 75], 5, 0)

pygame.draw.circle(screen, [0, 0, 0], [140, 75], 5, 0)

pygame.draw.polygon(screen, [255, 0, 0], [(155,85), (145, 85), (150, 100)])

pygame.display.flip()
