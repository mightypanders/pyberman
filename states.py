import setup
from constants import *
from entity import Player
from graphics.colors import *


class States(object):
	def __init__(self):
		self.done = False
		self.next = None
		self.quit = False
		self.previous = None


class Menu(States):
	def __init__(self):
		States.__init__(self)
		self.next = "game"

		self.bg_color = BACKGROUND

		self.font = MENU_FONT
		self.font_color = RED

		self.labels = []
		self.menu_items = ("Start", "Quit")

	def cleanup(self):
		self.labels = None
		print("do some cleanup")

	def startup(self):
		self.labels = []
		for item in self.menu_items:
			label = self.font.render(item, 1, self.font_color)
			self.labels.append(label)
		print("init menu stuff")

	def get_event(self, event):
		if event.type == pygame.QUIT:
			self.done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self.done = True

	def update(self, screen, dt):
		self.draw(screen)

	def draw(self, screen):
		screen.fill(self.bg_color)
		for index, label in enumerate(self.labels):
			screen.blit(label, ((index + 1) * 100, (index + 1) * 100))


class Loading(States):
	def __init__(self):
		States.__init__(self)


class Game(States):
	def __init__(self):
		States.__init__(self)
		self.next = "menu"
		self.all_sprites = pygame.sprite.Group()
		self.wall_list = pygame.sprite.Group()

		self.countHorBlock = 8
		self.countVertBlock = 10

		self.walls = setup.makeouterwalls(BLOCK, SCREEN_SIZE)
		self.blocks = setup.makeinnerblocks(BLOCK, SCREEN_SIZE,
		                                    self.countHorBlock,
		                                    self.countVertBlock)

		self.player = Player(PLAYER, 20, 20)

		self.wall_list.add(self.walls, self.blocks)
		self.all_sprites.add(self.wall_list, self.player)

		self.player.walls = self.wall_list

	def cleanup(self):
		print("do some game cleanup")

	def startup(self):
		print("startup game")

	def get_event(self, event):
		if event.type == pygame.QUIT:
			self.done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.player.changespeed(-3, 0)
			elif event.key == pygame.K_RIGHT:
				self.player.changespeed(3, 0)
			elif event.key == pygame.K_UP:
				self.player.changespeed(0, -3)
			elif event.key == pygame.K_DOWN:
				self.player.changespeed(0, 3)
			if event.key == pygame.K_SPACE:
				self.all_sprites.add(self.player.putbomb())
			if event.key == pygame.K_ESCAPE:
				self.done = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.player.changespeed(3, 0)
			elif event.key == pygame.K_RIGHT:
				self.player.changespeed(-3, 0)
			elif event.key == pygame.K_UP:
				self.player.changespeed(0, 3)
			elif event.key == pygame.K_DOWN:
				self.player.changespeed(0, -3)

	def update(self, screen, dt):
		self.draw(screen)
		self.all_sprites.update()

	def draw(self, screen):
		screen.fill(BACKGROUND)
		self.all_sprites.draw(SCREEN)


class Control:
	def __init__(self, **settings):
		self.__dict__.update(settings)
		self.done = False
		self.screen = SCREEN
		self.clock = CLOCK

	def setup_states(self, state_dict, start_state):
		self.state_dict = state_dict
		self.state_name = start_state
		self.state = self.state_dict[self.state_name]
		self.state.startup()

	def flip_state(self):
		self.state.done = False
		previous, self.state_name = self.state_name, self.state.next
		self.state.cleanup()
		self.state = self.state_dict[self.state_name]
		self.state.startup()
		self.state.previous = previous

	def update(self, dt):
		if self.state.quit:
			self.done = True
		elif self.state.done:
			self.flip_state()
		self.state.update(self.screen, dt)

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True
			self.state.get_event(event)

	def main_game_loop(self):
		while not self.done:
			delta_time = self.clock.tick(self.fps) / 1000.0
			self.event_loop()
			self.update(delta_time)
			pygame.display.update()


settings = {'fps': 60}

app = Control(**settings)
state_dict = {
	'menu': Menu(),
	'game': Game()
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
