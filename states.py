import setup
from constants import *
from entity import Player
from graphics.colors import *

pygame.init()


class States(object):
	def __init__(self):
		self.done = False
		self.next = None
		self.quit = False
		self.previous = None
		self.screen = SCREEN


class Menu(States):
	def __init__(self):
		States.__init__(self)
		self.next = "game"

		self.bg_color = MENUBACKGROUND

		self.font = MENU_FONT
		self.font_color = RED

		self.menu_items = ("Start", "Options", "Quit")

	def cleanup(self):
		self.labels = None
		print("do some cleanup")

	def startup(self):
		self.labels = []
		self.height_text = 0

		for index, item in enumerate(self.menu_items):

			label = self.font.render(item, 1, self.font_color)
			lbl_w, lbl_h = label.get_rect().width, label.get_rect().height

			self.height_text = len(self.menu_items)*lbl_h
			pos_x = (SCREEN_WIDTH / 2) - (lbl_w / 2)
			pos_y = (SCREEN_HEIGHT / 2) - (self.height_text / 2) + (
				index * lbl_h)
			self.labels.append([item, label, (lbl_w, lbl_h), (pos_x, pos_y)])

	def get_event(self, event):
		if event.type == pygame.QUIT:
			self.done, self.quit = True, True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self.done = True
			elif event.key == pygame.K_p:
				print(self.screen.get_rect().width, " ", self.screen.get_rect(
				).height)
			elif event.key == pygame.K_ESCAPE:
				self.done, self.quit = True, True

	def update(self, screen, dt):
		self.draw(screen)

	def draw(self, screen):
		screen.fill(self.bg_color)
		for item, label, (w, h), (x, y) in self.labels:
			self.screen.blit(label, (x, y))


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
		self.all_sprites = None
		self.wall_list = None
		self.walls = None
		self.blocks = None
		self.player = None

	def startup(self):
		self.__init__()

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
		screen.fill(GAMEBACKGROUND)
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
