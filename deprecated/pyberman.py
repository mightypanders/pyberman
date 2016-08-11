import setup
from constants import *
from entity import Player
from graphics.colors import *
from graphics.graphicshandler import *

DONE = False

all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

countHorBlock = 8
countVertBlock = 10

walls = setup.makeouterwalls(BLOCK, SCREEN_SIZE)
blocks = setup.makeinnerblocks(BLOCK, SCREEN_SIZE, countHorBlock,
                               countVertBlock)

player = Player(PLAYER, 20, 20)

wall_list.add(walls, blocks)
all_sprites.add(wall_list, player)

player.walls = wall_list
vidinfo = pygame.display.Info()
while not DONE:
	CLOCK.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			DONE = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_RIGHT:
				player.changespeed(3, 0)
			elif event.key == pygame.K_UP:
				player.changespeed(0, -3)
			elif event.key == pygame.K_DOWN:
				player.changespeed(0, 3)
			if event.key == pygame.K_SPACE:
				all_sprites.add(player.putbomb())
			if event.key == pygame.K_ESCAPE:
				print(vidinfo)
				DONE = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(3, 0)
			elif event.key == pygame.K_RIGHT:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_UP:
				player.changespeed(0, 3)
			elif event.key == pygame.K_DOWN:
				player.changespeed(0, -3)
	pygame.event.pump()

	all_sprites.update()

	SCREEN.fill(GAMEBACKGROUND)
	all_sprites.draw(SCREEN)
	pygame.display.flip()
