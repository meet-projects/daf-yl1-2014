import pygame
import sys

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 800))
	buttonimg = pygame.image.load('Background1.jpg')
	backsqr = pygame.Rect(0, 0 , 600, 800)
	main_screen.blit(buttonimg, backsqr)



	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			sys.exit()

		pygame.display.flip()