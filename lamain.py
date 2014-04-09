import pygame, sys, UIClasses, dafClasses

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

	angry=dafClasses.Emotion("50", "60", "Medium", (102,255,255), "Orange")
	anxious=dafClasses.Emotion("75", "90", "Large", (0,0,255), "Cherry")
	frustrated=dafClasses.Emotion("65", "60", "Medium", (76,0,153), "Lime")
	annoyed=dafClasses.Emotion("89", "120", "Large", (255, 102, 178), "Fruit Punch")
	isolated=dafClasses.Emotion("50", "45", "Medium", (255, 102, 102), "Raspberry")
	disappointed=dafClasses.Emotion("100", "120", "Large", (255, 0, 255), "Lemonade")
	abandoned=dafClasses.Emotion("95", "90", "Large", (255, 255, 102), "Green Tea")
	hurt=dafClasses.Emotion("59", "60", "Medium", (255, 153, 51), "Pineapple")
	sad=dafClasses.Emotion("102", "120", "Large", (0, 0, 204), "Apple")
	rejected=dafClasses.Emotion("76", "90", "Large", (0, 153, 76), "Pink Grapefruit")
	worried=dafClasses.Emotion("95", "120", "Large", (160, 160, 160), "Pear")
	bored=dafClasses.Emotion("68", "90", "Medium", (0, 102, 204) , "Mango")
	lonely=dafClasses.Emotion("64", "90", "Medium", (51, 255, 153), "Tropical Punch")
	depressed=dafClasses.Emotion("78", "60", "Large", (153, 0, 76), "Grape")


	button_angry = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "angry", angry.color)
	button_angry.setTextColor((0,0,0))
	button_angry.draw()

	button_anxious = UIClasses.Button(main_screen, background_color, 400, 150, 150 ,100, "anxious", anxious.color)
	button_anxious.setTextColor((0,0,0))
	button_anxious.draw()

	button_frustrated = UIClasses.Button(main_screen, background_color, 230, 270, 150 ,100, "frustrated", frustrated.color)
	button_frustrated.setTextColor((0,0,0))
	button_frustrated.draw()

	button_annoyed = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "annoyed", annoyed.color)
	button_annoyed.setTextColor((0,0,0))
	button_annoyed.draw()

	button_isolated = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "isolated", isolated.color)
	button_isolated.setTextColor((0,0,0))
	button_isolated.draw()

	button_disappointed = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "disappointed", disappointed.color)
	button_disappointed.setTextColor((0,0,0))
	button_disappointed.draw()

	button_abandoned = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "abandoned", abandoned.color)
	button_abandoned.setTextColor((0,0,0))
	button_abandoned.draw()


	button_hurt = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "hurt", hurt.color)
	button_hurt.setTextColor((0,0,0))
	button_hurt.draw()

	button_sad = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "sad", sad.color)
	button_sad.setTextColor((0,0,0))
	button_sad.draw()

	button_rejected = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "rejected", rejected.color)
	button_rejected.setTextColor((0,0,0))
	button_rejected.draw()

	button_worried = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "worried", worried.color)
	button_worried.setTextColor((0,0,0))
	button_worried.draw()

	button_bored = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "bored", bored.color)
	button_bored.setTextColor((0,0,0))
	button_bored.draw()

	button_lonely = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "lonely", lonely.color)
	button_lonely.setTextColor((0,0,0))
	button_lonely.draw()

	button_depressed = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "depressed", depressed.color)
	button_depressed.setTextColor((0,0,0))
	button_depressed.draw()

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

	sleepy = dafClasses.Powerup("120", "150", "Large", (255,255,0), "RedBull")
	lazy = dafClasses.Powerup("75", "60", "Medium", (0,0,255), "XL")
	exhausted = dafClasses.Powerup("95", "120", "Large", (0,255,0), "Monster")
	fatigued = dafClasses.Powerup("83", "75", "Medium", (76,0,153), "Blue")
	weak = dafClasses.Powerup("105", "90", "Large", (255,0,0), "Sparks")

	button_sleepy = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "sleepy", sleepy.color)
	button_sleepy.setTextColor((0,0,0))
	button_sleepy.draw()

	button_lazy = UIClasses.Button(main_screen, background_color, 400, 150, 150 ,100, "lazy", lazy.color)
	button_lazy.draw()

	button_exhausted = UIClasses.Button(main_screen, background_color, 230, 270, 150 ,100, "exhausted", exhausted.color)
	button_exhausted.setTextColor((44,69,169))
	button_exhausted.draw()
	
	button_fatigued = UIClasses.Button(main_screen, background_color, 70, 390, 150 ,100, "fatigued", fatigued.color)
	button_fatigued.setTextColor((255,255,0))
	button_fatigued.draw()

	button_weak = UIClasses.Button(main_screen, background_color, 400, 390, 150 ,100, "weak", weak.color)
	button_weak.draw()






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
