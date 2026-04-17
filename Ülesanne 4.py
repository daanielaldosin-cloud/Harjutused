import pygame
import random

# Mängu seadistus
LAIUS = 640
KORGUS = 480
FPS = 60

pygame.init()
aken = pygame.display.set_mode((LAIUS, KORGUS))
pygame.display.set_caption("Vastutulevad autod")
kell = pygame.time.Clock()

# Pildid laaditakse samast kaustast
taust = pygame.image.load("bg_rally.jpg")
taust = pygame.transform.scale(taust, (LAIUS, KORGUS))

punane_auto_pilt = pygame.image.load("f1_red.png")
sinine_auto_pilt = pygame.image.load("f1_blue.png")

# Tee sinise auto pilt sobivaks
AUTO_LAIUS = 50
AUTO_KORGUS = 90

punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, (AUTO_LAIUS, AUTO_KORGUS))
sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, (AUTO_LAIUS, AUTO_KORGUS))

# Tee sinine auto ülevalt alla (pööra 180°)
sinine_auto_pilt = pygame.transform.rotate(sinine_auto_pilt, 180)

# Punane auto — ekraani keskel allosas
punane_x = LAIUS // 2 - AUTO_LAIUS // 2
punane_y = KORGUS - AUTO_KORGUS - 20

# Tee fonk skoorile
font = pygame.font.SysFont("Arial", 28, bold=True)

# 3 kindlat sõidurada — keskpunktid tee peal (pildi põhjal)
RAJAD = [195, 315, 435]  # iga raja x-keskpunkt

# Tee sõiduraja piirid (ligikaudselt pildi põhjal)
# Rajad asuvad ekraani keskel
RAJA_VASAK = 180
RAJA_PAREM = 460


# Siniste autode klass
class SinineAuto:
    def __init__(self):
        self.laius = AUTO_LAIUS
        self.korgus = AUTO_KORGUS
        self.kiirus = random.randint(2, 5)
        self.taask2ivita()

    def taask2ivita(self):
        # Vali juhuslikult üks kolmest rajast
        raja_kesk = random.choice(RAJAD)
        self.x = raja_kesk - self.laius // 2
        self.y = random.randint(-300, -self.korgus)
        self.kiirus = random.randint(2, 5)

    def liiguta(self):
        self.y += self.kiirus

    def on_lahenud(self):
        return self.y > KORGUS

    def joonista(self, pind):
        pind.blit(sinine_auto_pilt, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.laius, self.korgus)


# Loo 5 sinist autot
sinised_autod = [SinineAuto() for _ in range(5)]

skoor = 0
toetab = True

while toetab:
    kell.tick(FPS)

    for syndmus in pygame.event.get():
        if syndmus.type == pygame.QUIT:
            toetab = False
        if syndmus.type == pygame.KEYDOWN:
            if syndmus.key == pygame.K_ESCAPE:
                toetab = False

    # Liiguta siniseid autosid
    for auto in sinised_autod:
        auto.liiguta()
        if auto.on_lahenud():
            skoor += 10  # Lisa skoorile punkte
            auto.taask2ivita()  # Alusta uuesti ülevalt

    # Joonista
    aken.blit(taust, (0, 0))

    for auto in sinised_autod:
        auto.joonista(aken)

    aken.blit(punane_auto_pilt, (punane_x, punane_y))

    # Skoor ekraanil
    skoor_tekst = font.render("Skoor: " + str(skoor), True, (255, 255, 0))
    aken.blit(skoor_tekst, (10, 10))

    pygame.display.flip()

pygame.quit()
