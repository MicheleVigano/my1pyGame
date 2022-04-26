from configparser import Interpolation
from re import X
from shutil import which
import pygame
import castles_war_constants as c

if __name__ == '__main__':
    # initialise pygame
    pygame.init()

    # events
    moving = pygame.USEREVENT + 0
    pygame.time.set_timer(moving, 2)

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
    GHIACCIOSOTTO_WIDTH = 70
    #
    ANGLE_ROT = 12 #piu alto piu gira veloce in teoria

    #position
    MURODESTRA_X = SCREEN_WIDTH
    MURODESTRA_Y = 0
    #
    BLOCCO1 = SCREEN_HEIGHT/2
    BLOCCO2 = SCREEN_HEIGHT/2
    dir = [0, 0]

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
    coso_img_flipl=pygame.image.load('img/Tiles/caneGreen.png').convert_alpha()
    coso_img_flipr = pygame.transform.flip(coso_img_flipl, True, False)
    palla_gif=pygame.image.load('img/palla.gif')



    # constants
    play = True
    INIT_RESOURCES = 10
    speed = [2, 1]
    pallarect = palla_gif.get_rect()
    
    # rotate image
    def palla_rotator():
      palla_gif =  pygame.transform.rotate(palla_gif, ANGLE_ROT)
      pass

    # # muovi blocco 1
    # def move1(moveTF):
    #   
    #   pass
  
################################################################## CICLO ##################################################################
    while play:
      
        # Background color
        screen.fill((0, 0, 0))

        pygame.display.set_caption('----------- ICEBRAKER -----------')

        # draw cursori
        screen.blit(coso_img_flipl, (GHIACCIOSOTTO_WIDTH,BLOCCO1))
        screen.blit(coso_img_flipr, (SCREEN_WIDTH - (GHIACCIOSOTTO_WIDTH*2),BLOCCO2))
        palla_rotator

        # lati
        for x in range(0, SCREEN_WIDTH, NEVESOTTO_WIDTH):
            screen.blit(muro_img, (0,x))
            screen.blit(muro_img, (SCREEN_WIDTH - NEVESOTTO_HEIGHT, x))
            screen.blit(ghiacciosotto_img_flipl, (0,x))
            screen.blit(ghiacciosotto_img_flipr, (SCREEN_WIDTH - NEVESOTTO_HEIGHT, x))
            screen.blit(ghiacciosotto_img_flipl, (0,x))
            screen.blit(ghiacciosotto_img_flipr, (SCREEN_WIDTH - NEVESOTTO_HEIGHT, x))

        # pavimento/soffitto
        for x in range(0, SCREEN_WIDTH, GHIACCIOSOTTO_WIDTH):
            screen.blit(ghiacciosotto_img, (x,SCREEN_HEIGHT - (GHIACCIOSOTTO_WIDTH+(NEVESOTTO_HEIGHT/7))))
            screen.blit(ghiacciosotto_img_flip, (x,NEVESOTTO_HEIGHT/7))
        for x in range(0, SCREEN_WIDTH, NEVESOTTO_WIDTH):
            screen.blit(nevesotto_img, (x,SCREEN_HEIGHT - NEVESOTTO_HEIGHT))
            screen.blit(nevesotto_img_flip, (x,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            
            
            #sposta 
            if event.type == pygame.KEYDOWN:##
               if event.key == pygame.K_q:
                   dir[0] = -1
               if event.key == pygame.K_a:
                   dir[0] = 1
               if event.key == pygame.K_p:
                   dir[1] = -1
               if event.key == pygame.K_l:
                   dir[1] = 1
            if event.type == pygame.KEYUP:##
               if event.key == pygame.K_q:
                  dir[0] = 0
               if event.key == pygame.K_a:
                   dir[0] = 0
               if event.key == pygame.K_p:
                   dir[1] = 0
               if event.key == pygame.K_l:
                   dir[1] = 0

            #move
            if event.type == moving:
                BLOCCO1 += dir[0]
                BLOCCO2 += dir[1]

            
        pallarect = pallarect.move(speed)
        if pallarect.left < 0 or pallarect.right > SCREEN_WIDTH:
             speed[0] = -speed[0]
        if pallarect.top < 0 or pallarect.bottom > SCREEN_HEIGHT:
           speed[1] = -speed[1]

        #screen.fill(black)
        screen.blit(palla_gif, pallarect)
    
 
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

