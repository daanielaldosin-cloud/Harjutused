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
pygame.display.set_caption("PingPong")
kell = pygame.time.Clock()

# Pildid
pall_pilt = pygame.image.load("ball.png").convert_alpha()
pall_pilt = pygame.transform.scale(pall_pilt, (20, 20))

alus_pilt = pygame.image.load("pad.png").convert_alpha()
alus_pilt = pygame.transform.scale(alus_pilt, (120, 20))

# Taustamuusika (pane muusikafail samasse kausta, nt "music.mp3")
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)  # Helitugevus: 0.0 (vaik) kuni 1.0 (max)
pygame.mixer.music.play(-1)  # -1 = korda lõputult

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
alus_y = int(KORGUS // 1.5)
alus_kiirus = 6

# Punktid
punktid = 0
font = pygame.font.SysFont(None, 36)
countdown_font = pygame.font.SysFont(None, 150)
gameover_font = pygame.font.SysFont(None, 80)


def countdown():
    for i in range(5, 0, -1):
        ekraan.fill(TAUST)
        ekraan.blit(pall_pilt, (pall_x, pall_y))
        ekraan.blit(alus_pilt, (alus_x, alus_y))
        tekst = countdown_font.render(str(i), True, (200, 0, 0))
        ekraan.blit(tekst, (LAIUS // 2 - tekst.get_width() // 2, KORGUS // 2 - tekst.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)


def game_over_ekraan():
    pygame.mixer.music.stop()
    ekraan.fill(TAUST)
    tekst1 = gameover_font.render("MANG LABI!", True, (200, 0, 0))
    tekst2 = font.render(f"Punktid: {punktid}", True, (0, 0, 0))
    tekst3 = font.render("Vajuta R - uuesti  /  Q - valju", True, (0, 0, 0))
    ekraan.blit(tekst1, (LAIUS // 2 - tekst1.get_width() // 2, KORGUS // 2 - 80))
    ekraan.blit(tekst2, (LAIUS // 2 - tekst2.get_width() // 2, KORGUS // 2 + 10))
    ekraan.blit(tekst3, (LAIUS // 2 - tekst3.get_width() // 2, KORGUS // 2 + 60))
    pygame.display.flip()

    while True:
        for sundmus in pygame.event.get():
            if sundmus.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if sundmus.type == pygame.KEYDOWN:
                if sundmus.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if sundmus.key == pygame.K_r:
                    main()
                    return


def joonista():
    ekraan.fill(TAUST)
    ekraan.blit(pall_pilt, (pall_x, pall_y))
    ekraan.blit(alus_pilt, (alus_x, alus_y))
    tekst = font.render(f"Punktid: {punktid}", True, (0, 0, 0))
    ekraan.blit(tekst, (10, 10))
    pygame.display.flip()


def main():
    global pall_x, pall_y, pall_kiirus_x, pall_kiirus_y
    global alus_x, punktid

    # Laesta manguolek
    pall_x = LAIUS // 2
    pall_y = KORGUS // 2
    pall_kiirus_x = 4
    pall_kiirus_y = 4
    alus_x = LAIUS // 2 - alus_laius // 2
    punktid = 0

    pygame.mixer.music.play(-1)

    countdown()

    jookseb = True
    while jookseb:
        kell.tick(FPS)

        for sundmus in pygame.event.get():
            if sundmus.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Aluse liikumine klaviatuuriga
        klahvid = pygame.key.get_pressed()
        if klahvid[pygame.K_LEFT]:
            alus_x -= alus_kiirus
        if klahvid[pygame.K_RIGHT]:
            alus_x += alus_kiirus

        # Alus ei lae valja piiridest
        if alus_x < 0:
            alus_x = 0
        if alus_x + alus_laius > LAIUS:
            alus_x = LAIUS - alus_laius

        # Palli liikumine
        pall_x += pall_kiirus_x
        pall_y += pall_kiirus_y

        # Pall porkub seinte vastu
        if pall_x <= 0 or pall_x + pall_suurus >= LAIUS:
            pall_kiirus_x = -pall_kiirus_x

        if pall_y <= 0:
            pall_kiirus_y = -pall_kiirus_y

        # Kokkupõrge alusega
        pall_rect = pygame.Rect(pall_x, pall_y, pall_suurus, pall_suurus)
        alus_rect = pygame.Rect(alus_x, alus_y, alus_laius, alus_korgus)

        if pall_rect.colliderect(alus_rect) and pall_kiirus_y > 0:
            pall_kiirus_y = -pall_kiirus_y
            punktid += 1

        # Pall kukkus alla - mang lopeb
        if pall_y + pall_suurus >= KORGUS:
            game_over_ekraan()
            return

        joonista()


if __name__ == "__main__":
    main()