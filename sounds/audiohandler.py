import pygame
import os

pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.mixer.init()
pygame.init()

class IngameSounds:
	def __init__(self):
		self.bomb_place = pygame.mixer.Sound("assets/bomb_place.ogg")
		self.bomb_explode = pygame.mixer.Sound("assets/explosion_1.ogg")
		self.walk_bump = pygame.mixer.Sound("assets/walk_bump.ogg")
		self.player_die = pygame.mixer.Sound("assets/player_die.ogg")
		self.item_pick = pygame.mixer.Sound("assets/item_pickup.ogg")
	# self.bad_item_pick = pygame.mixer.Sound("")
	# self.bomb_throw = pygame.mixer.Sound("")
	# self.bomb_pick_up = pygame.mixer.Sound("")


class MenuSounds:
	def __init__(self):
		self.menu_highlight = pygame.mixer.Sound("assets/select_menu_item.ogg")
		self.menu_pick = pygame.mixer.Sound("assets/confirm.ogg")
		# self.menu_invalid_pick = pygame.mixer.Sound("")
		# self.menu_scroll = pygame.mixer.Sound("")
		self.menu_start_game = pygame.mixer.Sound("assets/start_game.ogg")
