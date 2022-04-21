import pygame

GROUND_HEIGHT = 14
SCREEN_HEIGHT = 250
FINAL_HEIGHT = SCREEN_HEIGHT - GROUND_HEIGHT


class Wall:
    def __init__(self, image, WALL_POS):
        self.WALL_POS = WALL_POS
        self.WALL_WIDTH = 62
        self.WALL_HEIGHT = 80
        self.WALL_HEALTH = 1000
        self.IMAGE = image
        self.x = self.WALL_POS
        self.y = FINAL_HEIGHT - self.WALL_HEIGHT

    def draw(self, screen):
        screen.blit(self.IMAGE, (self.x, self.y))


class Mine:
    def __init__(self, image, MINE_POS):
        self.MINE_POS = MINE_POS
        self.MINE_WIDTH = 58
        self.MINE_HEIGHT = 37
        self.IMAGE = image
        self.x = self.MINE_POS
        self.y = FINAL_HEIGHT - self.MINE_HEIGHT

    def draw(self, screen):
        screen.blit(self.IMAGE, (self.x, self.y))


class Barracks:
    def __init__(self, image, BARRACKS_POS):
        self.BARRACKS_POS = BARRACKS_POS
        self.BARRACKS_WIDTH = 62
        self.BARRACKS_HEIGHT = 50
        self.IMAGE = image
        self.x = self.BARRACKS_POS
        self.y = FINAL_HEIGHT - self.BARRACKS_HEIGHT

    def draw(self, screen):
        screen.blit(self.IMAGE, (self.x, self.y))


class Worker(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.WORKER_COST = 1
        self.WORKER_TRAIN = 10
        self.WORKER_SPEED = 10
        self.WORKER_PROD = 1
        self.WORKER_REPAIR = 1
        self.IMAGE = image


class Swordsman(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.SWORD_COST = 5
        self.SWORD_TRAIN = 20
        self.SWORD_SPEED = 7
        self.SWORD_RANGE = 10
        self.SWORD_HIT = 2
        self.SWORD_REST = 10
        self.SWORD_HEALTH = 30
        self.IMAGE = image


class Archer(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.ARCHER_COST = 5
        self.ARCHER_TRAIN = 20
        self.ARCHER_RANGE = 100
        self.ARCHER_REST = 10
        self.ARCHER_HEALTH = 20
        self.ARCHER_HIT = 1
        self.IMAGE = image


# Arrow
ARROW_SPEED = 20  # distance covered in one turn by an arrow


class Tower(pygame.sprite.Sprite):
    def __init__(self, image, TOWER_POS):
        pygame.sprite.Sprite.__init__(self)
        self.TOWER_RANGE = 220
        self.TOWER_HIT = 5
        self.TOWER_REST = 5
        self.TOWER_HEIGHT = 160
        self.IMAGE = image
        self.TOWER_POS = TOWER_POS
        self.x = self.TOWER_POS
        self.y = FINAL_HEIGHT - self.TOWER_HEIGHT

    def draw(self, screen):
        screen.blit(self.IMAGE, (self.x, self.y))


# Keybord commands
PL1_WORKER_TRAIN = 'q'
PL1_SWORD_TRAIN = 'w'
PL1_ARCHER_TRAIN = 'e'
PL1_TO_MINE = 'a'
PL1_TO_WALL = 's'
PL1_SWORD_ATTACK = 'd'
PL1_ARCHER = 'f'
PL1_UNLEASH = 'z'

PL2_WORKER_TRAIN = 'p'
PL2_SWORD_TRAIN = 'o'
PL2_ARCHER_TRAIN = 'i'
PL2_TO_MINE = 'l'
PL2_TO_WALL = 'k'
PL2_SWORD_ATTACK = 'j'
PL2_ARCHER = 'h'
PL2_UNLEASH = 'm'

PAUSE = ' '
SAVE = 'V'
LOAD = 'B'