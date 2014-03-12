import pygame, sys

class Button(object):
	def __init__(self, screen ,screenBG, locationX, locationY, width = 100, height = 100, text = "", color = (0,0,0), visible = False):
		self.locationX = locationX
		self.locationY = locationY
		self.width = width
		self.height = height
		self.text = text
		self.color = color
		self.button_rec = pygame.Rect(self.locationX, self.locationY, self.width, self.height)
		self.button_sq = pygame.Surface([self.width, self.height])
		self.screenBG = screenBG
		self.screen = screen
		self.textColor = (255,255,255)

		self.visible = visible
	def setButtonColor(self, color):
		self.color = color
	def setTextColor(self, color):
		self.textColor = color 
	def draw(self):
		self.visible = True

		self.button_sq.fill(self.color)
		self.screen.blit(self.button_sq, self.button_rec)
		
		pygame.init()
		font=pygame.font.Font(None,25)
		fontSize = font.size(self.text)
		scoretext=font.render(self.text , 1, self.textColor)
		self.screen.blit(scoretext, (self.locationX + ((self.width - fontSize[0]) / 2) , self.locationY + ((self.height - fontSize[1]) / 2)))		
	def clear(self):
		self.visible = False

		self.button_sq.fill(self.screenBG)
		self.screen.blit(self.button_sq, self.button_rec)
	def click(self, x, y):
		return self.button_rec.collidepoint(x, y)

class Label(object):
	def __init__(self, screen, screenBG, text, locationX, locationY, fontSize = 15, fontColor = (0,0,0)):
		self.screen = screen
		self.screenBG = screenBG
		self.text = text
		self.locationX = locationX
		self.locationY = locationY
		self.fontSize = fontSize
		self.fontColor = fontColor
		self.size = {0 ,0}
	def draw(self):
		font = pygame.font.Font(None,self.fontSize)
		scoretext = font.render(self.text , 1 ,self.fontColor)
		self.size = font.size(self.text)
		self.screen.blit(scoretext, (self.locationX, self.locationY))

	def clear(self):
		button_rec = pygame.Rect(self.locationX, self.locationY, self.size[0], self.size[1])
		button_sq = pygame.Surface([self.size[0], self.size[1]])
		button_sq.fill(self.screenBG)
		self.screen.blit(button_sq, button_rec)
		

if (__name__ == "__main__"):
	main_screen = pygame.display.set_mode((600, 600))
	background_color = (255,255,0)
	main_screen.fill(background_color)
	button = Button(main_screen, background_color, 100, 100, 150, 100, "Hello", (0,0,0))
	button.draw()
	
	label = Label(main_screen, background_color, "yw4tywtqt", 200, 200 , 30, (255,0,0))
	label.draw()
	while True: 
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			x, y = ev.pos
			if button.click(x,y):
				print "(" + str(x) + ", " + str(y) + ")"
		# do something with the click
		pygame.display.flip()
