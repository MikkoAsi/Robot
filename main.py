import pygame
from random import randint
import time

pygame.init()
red, black, yellow, blue = (255, 0, 0), (0,0,0), (255,255,0), (0,255,255)
pisteet, huoneet = 0, 0
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("the Robot")

robo = pygame.image.load("robo.png")
r_x, r_y = 0, korkeus-robo.get_height()

oikealle = False
vasemmalle = False
ylos = False
alas = False

hirvio = pygame.image.load("hirvio.png")
h_x, h_y = leveys - hirvio.get_width(), korkeus-hirvio.get_height()
nopeus_h_x, nopeus_h_y  = 3, 3

h2_x, h2_y = 0, 0
nopeus_h2_x, nopeus_h2_y = 3, 3

h3_x, h3_y = 320, 0
nopeus_h3_x, nopeus_h3_y = 3, 3

h4_x, h4_y = leveys - hirvio.get_width(), 0
nopeus_h4_x, nopeus_h4_y = 3, 3

h5_x, h5_y = 320, korkeus-hirvio.get_height()
nopeus_h5_x, nopeus_h5_y = 3, 3

ovi = pygame.image.load("ovi.png")
def ovi_koordinaatit():
    x = randint(0,640-ovi.get_width())
    y = randint(30,480-ovi.get_height())
    return x, y
o_x, o_y = ovi_koordinaatit()

kolikko = pygame.image.load("kolikko.png")
def kolikko_koordinaatit():
    x = randint(0,640-kolikko.get_width())
    y = randint(30,480-kolikko.get_height())
    return x, y
k_x, k_y = kolikko_koordinaatit()

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
            if tapahtuma.key == pygame.K_DOWN:
                alas = True
            if tapahtuma.key == pygame.K_UP:
                ylos = True

            if tapahtuma.key == pygame.K_e:
                exit()

            if tapahtuma.key == pygame.K_n:
                pisteet, huoneet = 0, 1
                r_x, r_y = 0, korkeus-robo.get_height()
                h_x, h_y = leveys - hirvio.get_width(), korkeus-hirvio.get_height()
                k_x, k_y = kolikko_koordinaatit()

        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
            if tapahtuma.key == pygame.K_DOWN:
                alas = False
            if tapahtuma.key == pygame.K_UP:
                ylos = False

        if tapahtuma.type == pygame.QUIT:
            exit()

    if oikealle:
        r_x += 2
    if vasemmalle:
        r_x -= 2
    if ylos:
        r_y -= 2
    if alas:
        r_y += 2

    r_x = max(r_x, 0)
    r_x = min(r_x,leveys-robo.get_width())
    r_y = max(r_y,30)
    r_y = min(r_y,korkeus-robo.get_height())

    h_x += nopeus_h_x 
    h_y += nopeus_h_y
    if h_y + hirvio.get_height() >= 480:
        nopeus_h_y = -3   
    if h_x + hirvio.get_width() >= 640:
        nopeus_h_x = -3
    if h_y <= 30:
        nopeus_h_y = 3
    if h_x <= 0:
        nopeus_h_x = 3
    
    h2_x += nopeus_h2_x 
    h2_y += nopeus_h2_y
    if h2_y + hirvio.get_height() >= 480:
        nopeus_h2_y = -3   
    if h2_x + hirvio.get_width() >= 640:
        nopeus_h2_x = -3
    if h2_y <= 30:
        nopeus_h2_y = 3
    if h2_x <= 0:
        nopeus_h2_x = 3
    
    h3_x += nopeus_h3_x 
    h3_y += nopeus_h3_y
    if h3_y + hirvio.get_height() >= 480:
        nopeus_h3_y = -3   
    if h3_x + hirvio.get_width() >= 640:
        nopeus_h3_x = -3
    if h3_y <= 30:
        nopeus_h3_y = 3
    if h3_x <= 0:
        nopeus_h3_x = 3

    h4_x += nopeus_h4_x 
    h4_y += nopeus_h4_y
    if h4_y + hirvio.get_height() >= 480:
        nopeus_h4_y = -3   
    if h4_x + hirvio.get_width() >= 640:
        nopeus_h4_x = -3
    if h4_y <= 30:
        nopeus_h4_y = 3
    if h4_x <= 0:
        nopeus_h4_x = 3

    h5_x += nopeus_h5_x 
    h5_y += nopeus_h5_y
    if h5_y + hirvio.get_height() >= 480:
        nopeus_h5_y = -3   
    if h5_x + hirvio.get_width() >= 640:
        nopeus_h5_x = -3
    if h5_y <= 30:
        nopeus_h5_y = 3
    if h5_x <= 0:
        nopeus_h5_x = 3
    
    naytto.fill(black)

    if 0 <= pisteet < 5: # kolikoiden keräilyvaihe
        naytto.blit(kolikko, (k_x, k_y))
        if r_x <= k_x + kolikko.get_width()/2 <= r_x + robo.get_width() and r_y <= k_y + kolikko.get_height()/2 <= r_y + robo.get_height():
            pisteet += 1
            k_x, k_y = kolikko_koordinaatit()

    if pisteet == 5: # valot päälle ja ovi ilmestyy
        naytto.fill(yellow)
        naytto.blit(ovi, (o_x, o_y))
        if r_x <= o_x + ovi.get_width()/2 <= r_x + robo.get_width() and r_y <= o_y + ovi.get_height()/2 <= r_y + robo.get_height():
            pisteet = 0
            huoneet += 1
            o_x, o_y = ovi_koordinaatit()

    fontti = pygame.font.SysFont("Chalkboard", 24)
    teksti1 = fontti.render(f"Room: {huoneet}", True, red)
    naytto.blit(teksti1, (10, 3))
    teksti2 = fontti.render(f"Coins: {pisteet}", True, red)
    naytto.blit(teksti2, (110, 3))
    teksti3 = fontti.render(f"(n)ew game", True, red)
    naytto.blit(teksti3, (435, 3))
    teksti4 = fontti.render(f"(e)xit", True, red)
    naytto.blit(teksti4, (575, 3))

    naytto.blit(robo, (r_x, r_y))
    
    if huoneet == 0: # alkunäyttö
        naytto.fill(black)
        fontti = pygame.font.SysFont("Chalkboard", 36) 
        teksti1a = fontti.render(f"Get the Robot out of the Darkness", True, red)
        naytto.blit(teksti1a, (30, 120))
        teksti1b = fontti.render(f"and let's be careful out there...", True, red)
        naytto.blit(teksti1b, (30, 170))
        teksti2 = fontti.render(f"(n)ew game", True, red)
        naytto.blit(teksti3, (390, 325))
        teksti3 = fontti.render(f"(e)xit", True, red)
        naytto.blit(teksti4, (545, 325))
        naytto.blit(robo, (30, 270))

    if huoneet >= 1: # uusi huone & hirviöt + 1
        naytto.blit(hirvio, (h_x, h_y))
        if r_x <= h_x + hirvio.get_width()/2 <= r_x + robo.get_width() and r_y <= h_y + hirvio.get_height()/2 <= r_y + robo.get_height():
            time.sleep(2)
            huoneet = 0

    if huoneet >= 2: # uusi huone & hirviöt + 1
        naytto.blit(hirvio, (h2_x, h2_y))
        if r_x <= h2_x + hirvio.get_width()/2 <= r_x + robo.get_width() and r_y <= h2_y + hirvio.get_height()/2 <= r_y + robo.get_height():
            time.sleep(2)
            huoneet = 0
    
    if huoneet >= 3: # uusi huone & hirviöt + 1
        naytto.blit(hirvio, (h3_x, h3_y))
        if r_x <= h3_x + hirvio.get_width()/2 <= r_x + robo.get_width() and r_y <= h3_y + hirvio.get_height()/2 <= r_y + robo.get_height():
            time.sleep(2)
            huoneet = 0      

    if huoneet >= 4: # uusi huone & hirviöt + 1
        naytto.blit(hirvio, (h4_x, h4_y))
        if r_x <= h4_x + hirvio.get_width()/2 <= r_x + robo.get_width() and r_y <= h4_y + hirvio.get_height()/2 <= r_y + robo.get_height():
            time.sleep(2)
            huoneet = 0

    if huoneet >= 5: # uusi huone & hirviöt + 1
        naytto.blit(hirvio, (h5_x, h5_y))
        if r_x <= h5_x + hirvio.get_width()/2 <= r_x + robo.get_width() and r_y <= h5_y + hirvio.get_height()/2 <= r_y + robo.get_height():
            time.sleep(2)
            huoneet = 0

    if huoneet == 6: # viisi huonetta kierretty & peli pelattu läpi - lopunäyttö
        r_x, r_y = 0, 0
        nopeus_h_x, nopeus_h_y  = 0, 0
        nopeus_h2_x, nopeus_h2_y  = 0, 0
        nopeus_h3_x, nopeus_h3_y  = 0, 0
        nopeus_h4_x, nopeus_h4_y  = 0, 0
        nopeus_h5_x, nopeus_h5_y  = 0, 0
        naytto.fill(blue)
        fontti = pygame.font.SysFont("Chalkboard", 36)
        teksti1 = fontti.render(f"The Robot is FREE - well done :)", True, red)
        naytto.blit(teksti1, (30, 120))
        teksti2 = fontti.render(f"(n)ew game", True, red)
        naytto.blit(teksti3, (355, 235))
        teksti3 = fontti.render(f"(e)xit", True, red)
        naytto.blit(teksti4, (510, 235))
        naytto.blit(robo, (30, 180))

    pygame.display.flip()

    kello.tick(60)
