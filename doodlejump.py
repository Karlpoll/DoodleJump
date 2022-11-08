import pygame


pygame.init()

#kõik asjad, esemed ja muud tegelased, kes siin mängus on
width = 400
height = 600
fps = 60
font = pygame.font.SysFont('comicsansms', 20)
timer = pygame.time.Clock()
playerimage = pygame.transform.scale(pygame.image.load('tudeng1.png'), (80, 100))
background = 'white' #praegu on lht valge, IDEAALIS VÕIKS TEKKIDA MINGI MUSTER/GRADIENT
black = (0,0,0)

#muutujad
playerx = 100
playery = 400
playerchange = 0
platform = [[175, 400, 80, 10]]
jump = False
ychange = 0

window = pygame.display.set_mode((width, height)) #mängu akna suurus
pygame.display.set_caption('lõbus mäng masenduses tudengi kohta') 

#icon = pygame.image.load() IKOON VEEL VAJA KUJUNDADA
#pygame.set_icon(icon)

def updateplayer(y):
    global jump
    global ychange
    jumpheight = 10
    gravity = 1
    if jump:
        ychange -= 10
        jump = False
        y += ychange
        ychange += gravity
        return y


running = True
while running:
    timer.tick(fps)
    window.fill(background)
    window.blit(playerimage, (playerx, playery))
    blocks = []

    for i in range(len(platform)):
        block = pygame.draw.rect(window, black, platform[i], 1, 2)
        blocks.append(block)


    pygame.display.update()  #pakime mängu kokku ja lähme koju
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            running = False
#            sys.exit()