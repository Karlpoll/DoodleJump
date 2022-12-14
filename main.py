import pygame
import os

WIDTH, HEIGHT = 410, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jumpi Stiilis mäng!")

BEEŽ = (218, 203, 129)

#KONSTANTSED VÄÄRTUSED
FPS = 60
LIIKUMIS_KIIRUS = 5 #mängija liikumiskiirus paremale/vasakule
HÜPPE_KIIRUS = 10
GRAVITATSIOON = 3
MÄNGIJA_LAIUS, MÄNGIJA_PIKKUS = 40, 60

def draw_window(mängija): #JOONISTAB MÄNGIJA KARAKTERI EKRAANILE
    WIN.fill(BEEŽ)  
    WIN.blit(PLAYER_IMAGE, (mängija.x, mängija.y))
    
    pygame.display.update()

PLAYER_IMAGE = pygame.image.load(os.path.join("Assets", "Player.png")) #MÄNGIJA karakteri pildi fail
PLATFORM_IMAGE = pygame.image.load(os.path.join("Assets", "Platform.png")) #PLATVORMI pildi fail

def mängija_liikumine(vajutatud_klahvid, mängija):
    if vajutatud_klahvid[pygame.K_LEFT]: #VASAK
        mängija.x -= LIIKUMIS_KIIRUS
    if vajutatud_klahvid[pygame.K_RIGHT]: #PAREM
        mängija.x += LIIKUMIS_KIIRUS

#MÄNGU PÕHILOOP
def main():
    mängija = pygame.Rect(200, 350, MÄNGIJA_LAIUS, MÄNGIJA_PIKKUS)


    clock = pygame.time.Clock()
    work = True
    while work:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                work = False

        vajutatud_klahvid = pygame.key.get_pressed()
        mängija_liikumine(vajutatud_klahvid, mängija)
        draw_window(mängija)    
    
    pygame.quit()

if __name__ == "__main__":
    main()