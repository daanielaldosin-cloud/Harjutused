import pygame
import sys

# Initsialiseerimine
pygame.init()

# Mängu seaded
LAIUS = 640
KORGUS = 480
FPS = 60

# Värvid
TAUST = (200, 230, 255)  # Heledam taustavärv

# Ekraan
ekraan = pygame.display.set_mode((LAIUS, KORGUS))
pygame.display.set_caption("Pall ja Alus")
kell = pygame.time.Clock()

# Pildid
pall_pilt = pygame.image.load("ball.png").convert_alpha()
pall_pilt = pygame.transform.scale(pall_pilt, (20, 20))

alus_pilt = pygame.image.load("pad.png").convert_alpha()
alus_pilt = pygame.transform.scale(alus_pilt, (120, 20))

# Palli seaded
pall_suurus = 20
pall_x = LAIUS // 2
pall_y = KORGUS // 2
pall_kiirus_x = 4
pall_kiirus_y = 4

# Aluse seaded
alus_laius = 120
alus_korgus = 20
alus_x = LAIUS // 2 - alus_laius // 2
alus_y = KORGUS // 1.5  # y-koordinaat on keskkohast allpool
alus_kiirus = 6

# Punktid
punktid = 0
font = pygame.font.SysFont(None, 36)


def joonista():
    ekraan.fill(TAUST)

    # Joonista pall
    ekraan.blit(pall_pilt, (pall_x, pall_y))

    # Joonista alus
    ekraan.blit(alus_pilt, (alus_x, alus_y))

    # Kuva punktid ülemises nurgas
    tekst = font.render(f"Punktid: {punktid}", True, (0, 0, 0))
    ekraan.blit(tekst, (10, 10))

    pygame.display.flip()


def main():
    global pall_x, pall_y, pall_kiirus_x, pall_kiirus_y
    global alus_x
    global punktid

    jookseb = True

    while jookseb:
        kell.tick(FPS)

        # Sündmuste töötlemine
        for sundmus in pygame.event.get():
            if sundmus.type == pygame.QUIT:
                jookseb = False

        # Aluse liikumine klaviatuuriga
        klahvid = pygame.key.get_pressed()
        if klahvid[pygame.K_LEFT]:
            alus_x -= alus_kiirus
        if klahvid[pygame.K_RIGHT]:
            alus_x += alus_kiirus

        # Aluse piirid (vahetab suunda, kui puudub seinu)
        if alus_x < 0:
            alus_x = 0
        if alus_x + alus_laius > LAIUS:
            alus_x = LAIUS - alus_laius

        # Palli liikumine
        pall_x += pall_kiirus_x
        pall_y += pall_kiirus_y

        # Pall põrkub seinte vastu
        if pall_x <= 0 or pall_x + pall_suurus >= LAIUS:
            pall_kiirus_x = -pall_kiirus_x

        if pall_y <= 0:
            pall_kiirus_y = -pall_kiirus_y

        # Kokkupõrge alusega
        pall_rect = pygame.Rect(pall_x, pall_y, pall_suurus, pall_suurus)
        alus_rect = pygame.Rect(alus_x, alus_y, alus_laius, alus_korgus)

        if pall_rect.colliderect(alus_rect) and pall_kiirus_y > 0:
            pall_kiirus_y = -pall_kiirus_y
            punktid += 1  # Positiivne punkt, kui pall puutub alust

        # Pall kukkus alla (negatiivne punkt)
        if pall_y + pall_suurus >= KORGUS:
            punktid -= 1  # Negatiivne punkt, kui pall puudub alumist äärt
            # Taaskäivita pall keskelt
            pall_x = LAIUS // 2
            pall_y = KORGUS // 2
            pall_kiirus_y = abs(pall_kiirus_y)  # Liiku allapoole

        joonista()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()