import pygame, sys, UIClasses

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 800))
	#buttonimg = pygame.image.load('Background1.jpg')
	#backsqr = pygame.Rect(0, 0 , 600, 800)
	#main_screen.blit(buttonimg, backsqr)
	background_color = (171,124,240)
	main_screen.fill(background_color)

	button_E = UIClasses.Button(main_screen, background_color, 50, 100, 200 ,100, "Emotions", (25,0,51))
	button_E.draw()
	button_PU = UIClasses.Button(main_screen, background_color, 350, 100, 200 ,100, "Power Ups", (25,0,51))
	button_PU.draw()


	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x,y = ev.pos
			if button_E.click(x,y):
				button_E.clear()
			if button_PU.click(x,y):
				button_PU.clear()

		pygame.display.flip()