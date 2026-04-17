import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne 2")

bg = pygame.image.load("bg_shop.png")
screen.blit(bg, [0, 0])

seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [250, 300])
screen.blit(seller, [100, 150])


chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [260, 210])
screen.blit(chat, [245, 40])

font = pygame.font.Font(None, 34)
text = font.render("Tere, olen Daaniel", True, [255, 255, 255])
screen.blit(text, [280, 110])


pygame.display.flip()