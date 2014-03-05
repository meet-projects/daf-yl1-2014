import pygame, sys

class Button(object):
	def __init__(self, screen ,screenBG, locationX, locationY, width = 100, height = 100, text = "", color = (0,0,0)):
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
	def draw(self):
		self.button_sq.fill(self.color)
		self.screen.blit(self.button_sq, self.button_rec)
		
		pygame.init()	
		font=pygame.font.Font(None,25)
		scoretext=font.render(self.text , 1,(0,0,0))
		self.screen.blit(scoretext, (self.locationX + (self.width / 2) , self.locationY + (self.height / 2)))
		
	def clear(self):
		self.button_sq.fill(self.screenBG)
		self.screen.blit(self.button_sq, self.button_rec)
	def onClick(self, x, y):
		return self.button_rec.collidepoint(x, y)
		
		

if (__name__ == "__main__"):
	main_screen = pygame.display.set_mode((600, 600))
	background_color = (255,255,0)
	main_screen.fill(background_color)
	button = Button(main_screen, background_color, 100, 100, 150, 100, "Hello", (255,255,255))
	button.draw()
	while True: 
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			x, y = ev.pos
			if button.onClick(x,y):
				print "(" + str(x) + ", " + str(y) + ")"
		# do something with the click
		pygame.display.flip()
