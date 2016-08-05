import pygame

pygame.init()
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.HWACCEL

SCREEN = pygame.display.set_mode(SCREEN_SIZE, FLAGS)
CLOCK = pygame.time.Clock()

pygame.mouse.set_visible(False)

MENU_FONT = pygame.font.SysFont("Droid Sans Mono", 25)
