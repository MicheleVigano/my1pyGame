from configparser import Interpolation
from re import X
import pygame
import castles_war_constants as c

if __name__ == '__main__':
    # initialise pygame
    pygame.init()

    # program icon
    programIcon = pygame.image.load('img/icon_icebreaker.jpg')
    pygame.display.set_icon(programIcon)

    # game window specifications
    SCREEN_WIDTH = 920
    SCREEN_HEIGHT = 750

    # geometry
    BORDER = 10
    BUILDING_SEP = 5
    GROUND_HEIGHT = 10
    WALL_POS = 50
    WALL_WIDTH =80
    NEVESOTTO_Y = SCREEN_HEIGHT
    NEVESOTTO_WIDTH = 30
    NEVESOTTO_HEIGHT = 70

    #position
    MURODESTRA_X = SCREEN_WIDTH
    MURODESTRA_Y = 0
    #
    PALLA_X = SCREEN_WIDTH/2
    PALLA_Y = SCREEN_HEIGHT/2

    # create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))
    screen.fill((0, 255, 0), (0, screen.get_height() - GROUND_HEIGHT, screen.get_width(), 14))
    pygame.display.set_caption('ROMPIGHIACCIO')

    # images 
    muro_img=pygame.image.load('img/Tiles/iceWaterDeepStarsAlt.png').convert_alpha()
    nevesotto_img=pygame.image.load('img/Tiles/AsnowWave.png').convert_alpha()
    nevesotto_img_flip = pygame.transform.flip(nevesotto_img, False, True)
    ghiacciosotto_img=pygame.image.load('img/Tiles/spikesBottomAlt2.png').convert_alpha()
    ghiacciosotto_img_flip = pygame.transform.flip(ghiacciosotto_img, False, True)
    ghiacciosotto_img_flipl=pygame.image.load('img/Tiles/spikesBottomAlt.png').convert_alpha()
    ghiacciosotto_img_flipr = pygame.transform.flip(ghiacciosotto_img_flipl, True, False)
    palla_gif=pygame.image.load('img/palla.gif')



    # constants
    play = True
    INIT_RESOURCES = 10
    
    #background
    muro = c.Wall(muro_img, WALL_POS - WALL_WIDTH // 2)
    muro2 = c.Wall(muro_img, screen.get_width() - WALL_POS - WALL_WIDTH // 2)

  

    while play:
      
        # Background color
        screen.fill((0, 0, 0))

        pygame.display.set_caption('----------- ICEBRAKER -----------')

        # draw buildings
        muro.draw(screen)
        muro2.draw(screen)
        screen.blit(palla_gif, (PALLA_X,PALLA_Y))

        # lati
        for x in range(0, SCREEN_WIDTH, NEVESOTTO_WIDTH):
            screen.blit(ghiacciosotto_img_flipl, (0,x))
            screen.blit(ghiacciosotto_img_flipr, (SCREEN_WIDTH - NEVESOTTO_HEIGHT, x))
        # pavimento/soffitto
        for x in range(0, SCREEN_WIDTH, NEVESOTTO_WIDTH):
            screen.blit(nevesotto_img, (x,SCREEN_HEIGHT - NEVESOTTO_HEIGHT))
            screen.blit(nevesotto_img_flip, (x,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            
            #gravità
            

            #sposta 1 asse Y
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                PALLA_Y += 1

            #sposta 2 asse Y
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                PALLA_Y += 1
    
    
 
        # update display window
        pygame.display.update()
    pygame.quit()

## ROMPIGHIACCIO:: 2 muri di ghiaccio con faccia che ruota e trampolini che van su e giù, una volta vinta--> inserire il nome per conoscer vincitore/perdente e num di telefono




#   
#   
#   
#        inizializza ()
#   ### Ciclo Principale ###
#   while True:
#   # Avanzamento Base
#   basex -=
#   VEL AVANZ
#   if basex < -45: basex
#   # Gravità
#   uccello vely += 1
#   uccelloy += uccello_vely
#   # Comandi
#   for event in pygame.event.get() :
#   if event.type
#   uccello vely
#   if event.type
#   pygame.quit()
#   if uccelloy > 380|:
#   hai perso ()
#   # Aggiornamento Schermo
#   disegna oagetti()
#   aggiorna Ghe (7:01
#   pygame.KEYDOWN and event.key
#   = -10
#   pygame.K UP:
#   ==
#   ==
#   == pygame.QUIT:
#   HD
#   

