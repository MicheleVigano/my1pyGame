import pygame
import castles_war_constants as c

if __name__ == '__main__':
    # initialise pygame
    pygame.init()

    # game window specifications
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 250

    # geometry
    BORDER = 10
    BUILDING_SEP = 5
    GROUND_HEIGHT = 14
    WALL_POS = 180
    WALL_WIDTH = 62
    MINE_POS = 40
    MINE_WIDTH = 58
    BARRACKS_POS = 106
    BARRACKS_WIDTH = 62
    TOWER_WIDTH = 52

    # create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))
    screen.fill((0, 255, 0), (0, screen.get_height() - GROUND_HEIGHT, screen.get_width(), 14))
    pygame.display.set_caption('Castle War')

    # images player 1
    wall1_img = pygame.image.load('sprites/player1/building/wall.png').convert_alpha()
    mine1_img = pygame.image.load('sprites/player1/building/mine.png').convert_alpha()
    barracks1_img = pygame.image.load('sprites/player1/building/barracks.png').convert_alpha()
    # worker1_img = pygame.image.load('img/bg.png').convert_alpha()
    # swordsman1_img = pygame.image.load('img/bg.png').convert_alpha()
    # archer1_img = pygame.image.load('img/bg.png').convert_alpha()
    tower1_img = pygame.image.load('sprites/player1/building/tower.png').convert_alpha()

    # images player 2
    wall2_img = pygame.image.load('sprites/player2/building/wall.png').convert_alpha()
    mine2_img = pygame.image.load('sprites/player2/building/mine.png').convert_alpha()
    barracks2_img = pygame.image.load('sprites/player2/building/barracks.png').convert_alpha()
    # worker2_img = pygame.image.load('player1/img/bg.png').convert_alpha()
    # swordsman2_img = pygame.image.load('img/bg.png').convert_alpha()
    # archer2_img = pygame.image.load('img/bg.png').convert_alpha()
    tower2_img = pygame.image.load('sprites/player2/building/tower.png').convert_alpha()

    # constants
    play = True
    INIT_RESOURCES = 10
    mine1 = c.Mine(mine1_img, BORDER)
    mine2 = c.Mine(mine2_img, screen.get_width() - MINE_WIDTH - BORDER)
    barracks1 = c.Barracks(barracks1_img, BARRACKS_POS - BARRACKS_WIDTH // 2)
    barracks2 = c.Barracks(barracks2_img, screen.get_width() - BARRACKS_POS - BARRACKS_WIDTH // 2)
    tower1 = c.Tower(tower1_img, WALL_POS - TOWER_WIDTH // 2)
    tower2 = c.Tower(tower2_img, screen.get_width() - WALL_POS - TOWER_WIDTH // 2)
    wall1 = c.Wall(wall1_img, WALL_POS - WALL_WIDTH // 2)
    wall2 = c.Wall(wall2_img, screen.get_width() - WALL_POS - WALL_WIDTH // 2)

    while play:

        # draw buildings
        mine1.draw(screen)
        mine2.draw(screen)
        barracks1.draw(screen)
        barracks2.draw(screen)
        tower1.draw(screen)
        tower2.draw(screen)
        wall1.draw(screen)
        wall2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        # update display window
        pygame.display.update()

    pygame.quit()