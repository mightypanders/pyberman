import constants

class MenuItem():
	def __init__(self,text,pos):
		self.text = text
		self.label_item = constants.MENU_FONT.render(self.text, True,
		                                             constants.MENU_FONT_COLOR)
		self.pos_x = pos[0]
		self.pos_y = pos[1]
		self.width = self.label_item.get_rect().width
		self.height = self.label_item.get_rect().height

