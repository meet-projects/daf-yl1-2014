import pygame
import sys

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 800))
	main_screen.fill((151, 78, 174))



	while True: 
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT: 
            sys.exit()

        pygame.display.flip()