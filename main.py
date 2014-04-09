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
	global button_Cart
	
	label_Title = UIClasses.Label(main_screen, background_color, "What would you like to purchase today?", 75, 100, 35, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)
		
	button_Emontions.draw()
	onScreen.append(button_Emontions)

	button_PU.draw()
	onScreen.append(button_PU)

	button_Cart.draw()
	onScreen.append(button_Cart)
	
	
#Loads all the requierd buttons in the emotions screen
def emotionsScreen():
	global emotionsDict
	global onScreen		
	global main_screen
	global background_color
		
	global label_Title
	global button_back
		
	button_back.draw()
	onScreen.append(button_back)


	label_Title = UIClasses.Label(main_screen, background_color, "Emotions:", 200, 25, 50, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)

	emotionsDict["angry"] = dafClasses.Emotion("50", "60", "Medium", (102,255,255), "Orange")
	emotionsDict["anxious"] =dafClasses.Emotion("75", "90", "Large", (230,230,250), "Cherry")
	emotionsDict["frustrated"] =dafClasses.Emotion("65", "60", "Medium", (76,0,153), "Lime")
	emotionsDict["annoyed"] =dafClasses.Emotion("89", "120", "Large", (220,20,60), "Fruit Punch")
	emotionsDict["isolated"] =dafClasses.Emotion("50", "45", "Medium", (255, 102, 102), "Raspberry")
	emotionsDict["disappointed"] =dafClasses.Emotion("100", "120", "Large", (255, 0, 255), "Lemonade")
	emotionsDict["abandoned"] =dafClasses.Emotion("95", "90", "Large", (255, 255, 102), "Green Tea")
	emotionsDict["hurt"] =dafClasses.Emotion("59", "60", "Medium", (255, 153, 51), "Pineapple")
	emotionsDict["sad"] =dafClasses.Emotion("102", "120", "Large", (221,160,221), "Apple")
	emotionsDict["rejected"] =dafClasses.Emotion("76", "90", "Large", (0, 153, 76), "Pink Grapefruit")
	emotionsDict["worried"] =dafClasses.Emotion("95", "120", "Large", (160, 160, 160), "Pear")
	emotionsDict["bored"] =dafClasses.Emotion("68", "90", "Medium", (0, 102, 204) , "Mango")
	emotionsDict["lonely"] =dafClasses.Emotion("64", "90", "Medium", (51, 255, 153), "Tropical Punch")
	emotionsDict["depressed"] =dafClasses.Emotion("78", "60", "Large", (153, 0, 76), "Grape")

	emotionButtons = []

	button_angry = UIClasses.Button(main_screen, background_color, 70, 100, 130 ,80, "angry", emotionsDict["angry"].color)
	button_angry.setTextColor((0,0,0))
	emotionButtons.append(button_angry)
	onScreen.append(button_angry)

	button_anxious = UIClasses.Button(main_screen, background_color, 400, 100, 130 ,80, "anxious", emotionsDict["anxious"].color)
	button_anxious.setTextColor((0,0,0))
	emotionButtons.append(button_anxious)
	onScreen.append(button_anxious)


	button_frustrated = UIClasses.Button(main_screen, background_color, 230, 180, 130 ,80, "frustrated", emotionsDict["frustrated"].color)
	emotionButtons.append(button_frustrated)
	onScreen.append(button_frustrated)

	button_annoyed = UIClasses.Button(main_screen, background_color, 70, 250, 130 ,80, "annoyed", emotionsDict["annoyed"].color)
	emotionButtons.append(button_annoyed)
	onScreen.append(button_annoyed)

	button_isolated = UIClasses.Button(main_screen, background_color, 400, 250, 130 ,80, "isolated", emotionsDict["isolated"].color)
	button_isolated.setTextColor((0,0,0))
	emotionButtons.append(button_isolated)
	onScreen.append(button_isolated)

	button_disappointed = UIClasses.Button(main_screen, background_color, 230, 330, 130 ,80, "disappointed", emotionsDict["disappointed"].color)
	button_disappointed.setTextColor((0,0,0))
	emotionButtons.append(button_disappointed)
	onScreen.append(button_disappointed)

	button_abandoned = UIClasses.Button(main_screen, background_color, 70, 400, 130 ,80, "abandoned", emotionsDict["abandoned"].color)
	button_abandoned.setTextColor((0,0,0))
	emotionButtons.append(button_abandoned)
	onScreen.append(button_abandoned)

	button_hurt = UIClasses.Button(main_screen, background_color, 400, 400, 130 ,80, "hurt", emotionsDict["hurt"].color)
	button_hurt.setTextColor((0,0,0))
	emotionButtons.append(button_hurt)
	onScreen.append(button_hurt)

	button_sad = UIClasses.Button(main_screen, background_color, 230, 480, 130 ,80, "sad", emotionsDict["sad"].color)
	button_sad.setTextColor((0,0,0))
	emotionButtons.append(button_sad)
	onScreen.append(button_sad)

	button_rejected = UIClasses.Button(main_screen, background_color, 70, 550, 130 ,80, "rejected", emotionsDict["rejected"].color)
	button_rejected.setTextColor((0,0,0))
	emotionButtons.append(button_rejected)
	onScreen.append(button_rejected)

	button_worried = UIClasses.Button(main_screen, background_color, 400, 550, 130 ,80, "worried", emotionsDict["worried"].color)
	button_worried.setTextColor((0,0,0))
	emotionButtons.append(button_worried)
	onScreen.append(button_worried)

	button_bored = UIClasses.Button(main_screen, background_color, 230, 630, 130 ,80, "bored", emotionsDict["bored"].color)
	button_bored.setTextColor((0,0,0))
	emotionButtons.append(button_bored)
	onScreen.append(button_bored)

	button_lonely = UIClasses.Button(main_screen, background_color, 70, 700, 130 ,80, "lonely", emotionsDict["lonely"].color)
	button_lonely.setTextColor((0,0,0))
	emotionButtons.append(button_lonely)
	onScreen.append(button_lonely)

	button_depressed = UIClasses.Button(main_screen, background_color, 400, 700, 130 ,80, "depressed", emotionsDict["depressed"].color)
	emotionButtons.append(button_depressed)
	onScreen.append(button_depressed)
	
	for button in emotionButtons:
		button.draw()

#Loads all the requierd buttons in the power ups screen
def PUScreen():
	global onScreen		
	global main_screen
	global background_color
		
	global label_Title
	global button_back

	global PUDict
	
	button_back.draw()
	onScreen.append(button_back)

	label_Title = UIClasses.Label(main_screen, background_color, "Power Ups:", 200, 100, 50, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)

	PUDict["sleepy"] = dafClasses.Powerup("120", "150", "Large", (255,255,0), "RedBull")
	PUDict["lazy"] = dafClasses.Powerup("75", "60", "Medium", (0,0,255), "XL")
	PUDict["exhausted"] = dafClasses.Powerup("95", "120", "Large", (0,255,0), "Monster")
	PUDict["fatigued"] = dafClasses.Powerup("83", "75", "Medium", (76,0,153), "Blue")
	PUDict["weak"] = dafClasses.Powerup("105", "90", "Large", (255,0,0), "Sparks")

	PUButtons = []

	button_sleepy = UIClasses.Button(main_screen, background_color, 70, 150, 150 ,100, "sleepy", PUDict["sleepy"].color)
	button_sleepy.setTextColor((0,0,0))
	onScreen.append(button_sleepy)
	PUButtons.append(button_sleepy)

	button_lazy = UIClasses.Button(main_screen, background_color, 400, 150, 150 ,100, "lazy", PUDict["lazy"].color)
	onScreen.append(button_lazy)
	PUButtons.append(button_lazy)


	button_exhausted = UIClasses.Button(main_screen, background_color, 230, 270, 150 ,100, "exhausted", PUDict["exhausted"].color)
	button_exhausted.setTextColor((44,69,169))
	onScreen.append(button_exhausted)
	PUButtons.append(button_exhausted)

	
	button_fatigued = UIClasses.Button(main_screen, background_color, 70, 390, 150 ,100, "fatigued", PUDict["fatigued"].color)
	button_fatigued.setTextColor((255,255,0))
	onScreen.append(button_fatigued)
	PUButtons.append(button_fatigued)


	button_weak = UIClasses.Button(main_screen, background_color, 400, 390, 150 ,100, "weak", PUDict["weak"].color)
	onScreen.append(button_weak)
	PUButtons.append(button_weak)

	for button in PUButtons:
		button.draw()


def viewProductScreen():
	global label_Title
	global main_screen
	global button_plus
	global button_minus	
	global button_addToCart
	global isAddToCartSlide
	global counterLabel
	
	isAddToCartSlide = True
	productBG = (255,0,0)
	main_screen.fill(productBG)

	label_Title = UIClasses.Label(main_screen, background_color, "Product name", 75, 100, 35, (25,0,51))
	label_Title.draw()
	onScreen.append(label_Title)

	button_back.draw()
	onScreen.append(button_back)
	
	
	button_plus.draw()
	onScreen.append(button_plus)
	
	button_minus.draw()
	onScreen.append(button_minus)

	button_addToCart.draw()
	onScreen.append(button_addToCart)

	counterLabel.draw()
	onScreen.append(counterLabel)
		
	
#Initialize everythings before starting to work with the UI. MUST BE CALLED AT THE BEGGINIG OF THE PROGRAM
def initialize():
	global onScreen		
	global main_screen
	global background_color
	
	global emotionsDict
	global PUDict
	global cart
	global isAddToCartSlide

	global label_Title
	global button_Emontions
	global button_PU
	global button_back
	global button_Cart

	global button_plus
	global button_minus
	global button_addToCart
	global counterLabel

	pygame.init()
	main_screen = pygame.display.set_mode((600, 800))
		
	background_color = (171,124,240)
	main_screen.fill(background_color)
	onScreen = []
	
	emotionsDict = {}
	PUDict = {}
	cart = []
	isAddToCartSlide = False
	
	label_Title = UIClasses.Label(main_screen, background_color, "What would you like to purchase today?", 75, 100, 35, (25,0,51))	
	button_Emontions = UIClasses.Button(main_screen, background_color, 50, 200, 500 ,160, "Emotions", (25,0,51))
	button_Emontions.setTextSize(40)
	button_PU = UIClasses.Button(main_screen, background_color, 50, 450, 500 ,160, "Power Ups", (25,0,51))
	button_PU.setTextSize(40)
	button_back = UIClasses.Button(main_screen, background_color, 20, 20, 100 ,66 , "Back", (25,0,51))
	button_Cart = UIClasses.Button(main_screen, background_color, 480, 650, 100 ,66 , "Cart", (35,0,51))

	button_plus = UIClasses.Button(main_screen, background_color, 160, 200, 80 ,80 , "+", (35,0,51))
	button_minus = UIClasses.Button(main_screen, background_color, 360, 200, 80 ,80 , "-", (35,0,51))

	counterLabel = UIClasses.Button(main_screen, background_color, 260, 200, 80 ,80 , "0", (255,75,255)) ## was made as button for the background. click functions is not implemented!!!

	button_addToCart = UIClasses.Button(main_screen, background_color, 100, 320, 400 ,200 , "Add to cart!", (35,0,51))
	button_addToCart.setTextSize(40)
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
				if(isAddToCartSlide):
					main_screen.fill(background_color)
					counterLabel.text = "0";
					counterLabel.draw()
					isAddToCartSlide = False					
				clearScreen()
				mainScreen()
			if button_Cart.visible and button_Cart.click(x, y):
				clearScreen()
				viewProductScreen()
			if button_plus.visible and button_plus.click(x, y):
				newValue = int(counterLabel.text) + 1
				counterLabel.text = str(newValue);
				counterLabel.draw()
			if button_minus.visible and button_minus.click(x, y):
				newValue = int(counterLabel.text) - 1
				if newValue >= 0:
					counterLabel.text = str(newValue);
					counterLabel.draw()
				
		pygame.display.flip()
