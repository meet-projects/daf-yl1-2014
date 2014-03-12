import pygame, sys, UIClasses

#Clears all the UI objects that on the screen
def clearScreen():			
	global onScreen
	for UIObject in onScreen:
		UIObject.clear()
	onScreen = []

#Loads all the requierd buttons in the main screen
def mainScreen():
	global onScreen		
	global main_screen
	global background_color

	global label_Title
	global button_Emontions
	global button_PU
	
	label_Title = UIClasses.Label(main_screen, background_color, "What would you like to purchase today?", 75, 100, 35, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)
		
	button_Emontions.draw()
	onScreen.append(button_Emontions)

	button_PU.draw()
	onScreen.append(button_PU)
#Loads all the requierd buttons in the emotions screen
def emotionsScreen():
	global onScreen		
	global main_screen
	global background_color
		
	global label_Title
	global button_back
		
	button_back.draw()
	onScreen.append(button_back)

	label_Title = UIClasses.Label(main_screen, background_color, "Emotions:", 200, 100, 50, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)
#Loads all the requierd buttons in the power ups screen
def PUScreen():
	global onScreen		
	global main_screen
	global background_color
		
	global label_Title
	global button_back
	
	button_back.draw()
	onScreen.append(button_back)

	label_Title = UIClasses.Label(main_screen, background_color, "Power Ups:", 200, 100, 50, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)

#Initialize everythings before starting to work with the UI. MUST BE CALLED AT THE BEGGINIG OF THE PROGRAM
def initialize():
	global onScreen		
	global main_screen
	global background_color

	global label_Title
	global button_Emontions
	global button_PU
	global button_back

	pygame.init()
	main_screen = pygame.display.set_mode((600, 800))
	#buttonimg = pygame.image.load('Background1.jpg')
	#backsqr = pygame.Rect(0, 0 , 600, 800)
	#main_screen.blit(buttonimg, backsqr)
	background_color = (171,124,240)
	main_screen.fill(background_color)
	onScreen = []
	
	label_Title = UIClasses.Label(main_screen, background_color, "What would you like to purchase today?", 75, 100, 35, (25,0,51))	
	button_Emontions = UIClasses.Button(main_screen, background_color, 50, 200, 500 ,200, "Emotions", (25,0,51))
	button_PU = UIClasses.Button(main_screen, background_color, 50, 500, 500 ,200, "Power Ups", (25,0,51))
	button_back = UIClasses.Button(main_screen, background_color, 20, 20, 100 ,66 , "Back", (25,0,51))

if __name__=="__main__":
	initialize()
	mainScreen()

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x,y = ev.pos
			if button_Emontions.visible and button_Emontions.click(x,y):
				clearScreen()
				emotionsScreen()
			if button_PU.visible and button_PU.click(x,y):
				clearScreen()
				PUScreen()
			if button_back.visible and button_back.click(x, y):
				clearScreen()
				mainScreen()
		pygame.display.flip()
