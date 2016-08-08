import pygame

pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.mixer.init()
pygame.init()


class ingamesounds:
	def __init__(self):
		self.bomb_place = pygame.mixer.Sound("sounds/bomb_place.ogg")
		self.bomb_explode = pygame.mixer.Sound("sounds/explosion_1.ogg")
		# self.walk_step = pygame.mixer.Sound("")
		self.walk_bump = pygame.mixer.Sound("sounds/walk_bump.ogg")
		self.player_die = pygame.mixer.Sound("sounds/player_die.ogg")
		self.item_pick = pygame.mixer.Sound("sounds/item_pickup.ogg")

	# self.bad_item_pick = pygame.mixer.Sound("")
	# self.bomb_throw = pygame.mixer.Sound("")
	# self.bomb_pick_up = pygame.mixer.Sound("")


class menusounds:
	def __init__(self):
		self.menu_highlight = pygame.mixer.Sound("sounds/select_menu_item.ogg")
		self.menu_pick = pygame.mixer.Sound("sounds/confirm.ogg")

		# self.menu_invalid_pick = pygame.mixer.Sound("")
		# self.menu_scroll = pygame.mixer.Sound("")
		self.menu_start_game = pygame.mixer.Sound("sounds/start_game.ogg")
