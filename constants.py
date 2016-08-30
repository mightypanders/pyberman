import pygame
from graphics.colors import *

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.HWACCEL

SCREEN = pygame.display.set_mode(SCREEN_SIZE, FLAGS)
CLOCK = pygame.time.Clock()



MENU_FONT = pygame.font.SysFont("Droid Sans Mono", 25)
MENU_FONT_COLOR = RED
