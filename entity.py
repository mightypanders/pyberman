from datetime import datetime

import pygame

from sounds.audiohandler import IngameSounds

wall_width = 10
sounds = IngameSounds()


class Player(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		super().__init__()
		self.image = pygame.Surface([20, 20])
		self.color = color
		self.image.fill(self.color)

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

		self.changex = 0
		self.changey = 0
		self.walls = None

		self.bomb_color = self.color
		self.bombs = pygame.sprite.Group()
		self.bomb_max = 5
		self.bombs_placed = len(self.bombs)

	def changespeed(self, x, y):
		self.changex += x
		self.changey += y

	def update(self):
		self.rect.x += self.changex
		block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
		for block in block_hit_list:
			if self.changex > 0:
				self.rect.right = block.rect.left
			elif self.changex < 0:
				self.rect.left = block.rect.right

		self.rect.y += self.changey
		block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
		for block in block_hit_list:
			if self.changey > 0:
				self.rect.bottom = block.rect.top
			elif self.changey < 0:
				self.rect.top = block.rect.bottom

		self.bombs_placed = len(self.bombs)

	def putbomb(self):
		if self.bomb_max > self.bombs_placed:
			sounds.bomb_place.play()
			print("bombe hier")
			newbomb = Bomb(self.bomb_color, self)
			self.bombs_placed += 1
			self.bombs.add(newbomb)
			print(self.bombs)
			return self.bombs
		else:
			print("keine bombe")
			return self.bombs

	def bomb_exploded(self):
		self.bombs_placed -= 1


class Bomb(pygame.sprite.Sprite):
	def __init__(self, color, player):
		super().__init__()
		self.image = pygame.Surface([10, 10])
		self.image.fill(color)
		self.player = player
		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x
		self.rect.y = player.rect.y
		self.timeplaced = datetime.now()

	def update(self):
		delta = (datetime.now() - self.timeplaced).seconds
		if delta > 3:
			self.explode()

	def explode(self):
		sounds.bomb_explode.play()
		self.kill()
		print(self.player.bombs_placed)


class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
