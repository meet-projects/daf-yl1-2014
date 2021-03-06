import pygame, sys, UIClasses, dafClasses

#Clears all the UI objects that on the screen
def clearScreen():			
	global onScreen
	for UIObject in onScreen:
		UIObject.clear()
	onScreen = []

#Loads all the required buttons in the main screen
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
	global emotionButtons

	global onScreen		
	global main_screen
	global background_color
		
	global label_Title
	global button_back
	
		
	button_back.draw()
	onScreen.append(button_back)


	label_Title = UIClasses.Label(main_screen, background_color, "Which Emotion would", 150, 25, 50, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)

	label_Title2 = UIClasses.Label(main_screen, background_color, "you like to solve?", 170, 80, 50, (25,0,51))
	label_Title2.draw()
	onScreen.append(label_Title2)

	emotionsDict["Angry"] = dafClasses.Emotion("Angry", 50, 60, "Medium", (102,255,255), "Orange")
	emotionsDict["Frustrated"] =dafClasses.Emotion("Frustrated", 65, 60, "Medium", (76,0,153), "Lime")
	emotionsDict["Annoyed"] =dafClasses.Emotion("Annoyed", 89, 120, "Large", (220,20,60), "Fruit Punch")
	emotionsDict["Isolated"] =dafClasses.Emotion("Isolated", 50, 45, "Medium", (255, 102, 102), "Raspberry")
	emotionsDict["Disappointed"] =dafClasses.Emotion("Disappointed", 100, 120, "Large", (255, 0, 255), "Lemonade")
	emotionsDict["Hurt"] =dafClasses.Emotion("Hurt", 59, 60, "Medium", (255, 153, 51), "Pineapple")
	emotionsDict["Sad"] =dafClasses.Emotion("Sad", 102, 120, "Large", (221,160,221), "Apple")
	emotionsDict["Rejected"] =dafClasses.Emotion("Rejected", 76, 90, "Large", (0, 153, 76), "Pink Grapefruit")
	emotionsDict["Worried"] =dafClasses.Emotion("Worried", 95, 120, "Large", (160, 160, 160), "Pear")
	emotionsDict["Bored"] =dafClasses.Emotion("Bored", 68, 90, "Medium", (0, 102, 204) , "Mango")
	emotionsDict["Lonely"] =dafClasses.Emotion("Lonely", 64, 90, "Medium", (51, 255, 153), "Tropical Punch")
	emotionsDict["Depressed"] =dafClasses.Emotion("Depressed", 78, 60, "Large", (153, 0, 76), "Grape")

	button_angry = UIClasses.Button(main_screen, background_color, 70, 150, 130 ,80, "Angry", emotionsDict["Angry"].color)
	button_angry.setTextColor((0,0,0))
	emotionButtons.append(button_angry)
	onScreen.append(button_angry)

	button_frustrated = UIClasses.Button(main_screen, background_color, 230, 150, 130 ,80, "Frustrated", emotionsDict["Frustrated"].color)
	emotionButtons.append(button_frustrated)
	onScreen.append(button_frustrated)

	button_isolated = UIClasses.Button(main_screen, background_color, 400, 150, 130 ,80, "Isolated", emotionsDict["Isolated"].color)
	button_isolated.setTextColor((0,0,0))
	emotionButtons.append(button_isolated)
	onScreen.append(button_isolated)

	button_annoyed = UIClasses.Button(main_screen, background_color, 70, 300, 130 ,80, "Annoyed", emotionsDict["Annoyed"].color)
	emotionButtons.append(button_annoyed)
	onScreen.append(button_annoyed)

	button_disappointed = UIClasses.Button(main_screen, background_color, 230, 300, 130 ,80, "Disappointed", emotionsDict["Disappointed"].color)
	button_disappointed.setTextColor((0,0,0))
	emotionButtons.append(button_disappointed)
	onScreen.append(button_disappointed)

	button_hurt = UIClasses.Button(main_screen, background_color, 400, 300, 130 ,80, "Hurt", emotionsDict["Hurt"].color)
	button_hurt.setTextColor((0,0,0))
	emotionButtons.append(button_hurt)
	onScreen.append(button_hurt)

	button_rejected = UIClasses.Button(main_screen, background_color, 70, 450, 130 ,80, "Rejected", emotionsDict["Rejected"].color)
	button_rejected.setTextColor((0,0,0))
	emotionButtons.append(button_rejected)
	onScreen.append(button_rejected)

	button_sad = UIClasses.Button(main_screen, background_color, 230, 450, 130 ,80, "Sad", emotionsDict["Sad"].color)
	button_sad.setTextColor((0,0,0))
	emotionButtons.append(button_sad)
	onScreen.append(button_sad)

	button_worried = UIClasses.Button(main_screen, background_color, 400, 450, 130 ,80, "Worried", emotionsDict["Worried"].color)
	button_worried.setTextColor((0,0,0))
	emotionButtons.append(button_worried)
	onScreen.append(button_worried)

	button_lonely = UIClasses.Button(main_screen, background_color, 70, 600, 130 ,80, "Lonely", emotionsDict["Lonely"].color)
	button_lonely.setTextColor((0,0,0))
	emotionButtons.append(button_lonely)
	onScreen.append(button_lonely)

	button_bored = UIClasses.Button(main_screen, background_color, 230, 600, 130 ,80, "Bored", emotionsDict["Bored"].color)
	button_bored.setTextColor((0,0,0))
	emotionButtons.append(button_bored)
	onScreen.append(button_bored)

	button_depressed = UIClasses.Button(main_screen, background_color, 400, 600, 130 ,80, "Depressed", emotionsDict["Depressed"].color)
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
	global PUButtons
	
	button_back.draw()
	onScreen.append(button_back)

	label_Title = UIClasses.Label(main_screen, background_color, "Power Ups:", 200, 50, 50, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)

	PUDict["Awake"] = dafClasses.Powerup("Awake", 120, 150, "Large", (255,255,0), "RedBull")
	PUDict["Diligent"] = dafClasses.Powerup("Diligent", 75, 60, "Medium", (0,0,255), "XL")
	PUDict["Energetic"] = dafClasses.Powerup("Energetic", 95, 120, "Large", (0,255,0), "Monster")
	PUDict["Concentrated"] = dafClasses.Powerup("Concentrated", 83, 75, "Medium", (76,0,153), "Blue")
	PUDict["Strong"] = dafClasses.Powerup("Strong", 105, 90, "Large", (255,0,0), "Sparks")

	button_sleepy = UIClasses.Button(main_screen, background_color, 60, 150, 150 ,100, "Awake", PUDict["Awake"].color)
	button_sleepy.setTextColor((0,0,0))
	onScreen.append(button_sleepy)
	PUButtons.append(button_sleepy)

	button_lazy = UIClasses.Button(main_screen, background_color, 400, 150, 150 ,100, "Diligent", PUDict["Diligent"].color)
	onScreen.append(button_lazy)
	PUButtons.append(button_lazy)


	button_exhausted = UIClasses.Button(main_screen, background_color, 230, 270, 150 ,100, "Energetic", PUDict["Energetic"].color)
	button_exhausted.setTextColor((0,0,0))
	onScreen.append(button_exhausted)
	PUButtons.append(button_exhausted)

	
	button_fatigued = UIClasses.Button(main_screen, background_color, 60, 390, 150 ,100, "Concentrated", PUDict["Concentrated"].color)
	button_fatigued.setTextColor((255,255,255))
	onScreen.append(button_fatigued)
	PUButtons.append(button_fatigued)


	button_weak = UIClasses.Button(main_screen, background_color, 400, 390, 150 ,100, "Strong", PUDict["Strong"].color)
	onScreen.append(button_weak)
	PUButtons.append(button_weak)

	for button in PUButtons:
		button.draw()


def viewProductScreen(product):
	global label_Title
	global main_screen
	global button_plus
	global button_minus	
	global button_addToCart
	global currentScreen
	global counterLabel
	global currentProduct
	
	currentProduct = product
	
	currentScreen = "viewProductScreen"
	main_screen.fill(product.color)

	label_Title = UIClasses.Label(main_screen, background_color, product.name, 75, 100, 35, (25,0,51))
	label_Title.draw()
	onScreen.append(label_Title)

	label_price = UIClasses.Label(main_screen, background_color, str(product.price) + " NIS", 75, 130, 35, (25,0,51))
	label_price.draw()
	onScreen.append(label_price)

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
	

def cartScreen():
	global onScreen		
	global main_screen
	global background_color
	global button_back
	global label_Title
	global button_buy

	button_back.draw()
	onScreen.append(button_back)

	label_Title = UIClasses.Label(main_screen, background_color, "Cart", 250, 70, 85, (25,0,51))	
	label_Title.draw()
	onScreen.append(label_Title)

	product_name = UIClasses.Label(main_screen, background_color, "Product name", 85, 180, 35, (25,0,51))	
	product_name.draw()
	onScreen.append(product_name)

	product_quantity = UIClasses.Label(main_screen, background_color, "Quantity", 300, 180, 35, (25,0,51))	
	product_quantity.draw()
	onScreen.append(product_quantity)

	button_buy = UIClasses.Button(main_screen, background_color, 150, 700, 300 ,100 , "Buy", (35,0,51))	
	button_buy.draw()
	onScreen.append(button_buy)


	product_price = UIClasses.Label(main_screen, background_color, "Price", 460, 180, 35, (25,0,51))	
	product_price.draw()
	onScreen.append(product_price)

	productCounter = 1;
	totalCost = 0;

	for cartProduct in cart:
		product_name = UIClasses.Label(main_screen, background_color, str(cartProduct.product.name), 85, 180 + (40 * productCounter), 35, (25,0,51))	
		product_name.draw()
		onScreen.append(product_name)

		product_quantity = UIClasses.Label(main_screen, background_color, str(cartProduct.quantity), 300, 180 + (40 * productCounter), 35 , (25,0,51))	
		product_quantity.draw()
		onScreen.append(product_quantity)

		product_price = UIClasses.Label(main_screen, background_color, str(int(cartProduct.product.price) * int(cartProduct.quantity)) + " NIS", 460, 180 + (40 * productCounter), 35, (25,0,51))
		product_price.draw()
		onScreen.append(product_price)

		totalCost = totalCost + int(cartProduct.product.price) * int(cartProduct.quantity)
		productCounter = productCounter + 1

	label_totalCost = UIClasses.Label(main_screen, background_color, "Total Cost: " + str(totalCost) + " NIS" , 350, 650, 35, (25,0,51))	
	label_totalCost.draw()
	onScreen.append(label_totalCost)

def thankYouScreen():
	label_thankYou = UIClasses.Label(main_screen, background_color, "Thank you!", 150, 180 , 80, (255,255,102))
	label_thankYou.draw()
	onScreen.append(label_thankYou)

	label_leen = UIClasses.Label(main_screen, background_color, "Leen", 150, 240 , 40, (25,0,51))
	label_leen.draw()
	onScreen.append(label_leen)

	label_aseel = UIClasses.Label(main_screen, background_color, "Aseel", 150, 280 , 40, (25,0,51))
	label_aseel.draw()
	onScreen.append(label_aseel)

	label_ophir = UIClasses.Label(main_screen, background_color, "Ophir", 150, 320 , 40, (25,0,51))
	label_ophir.draw()
	onScreen.append(label_ophir)

	label_mouhammed = UIClasses.Label(main_screen, background_color, "Mouhammed", 150, 360 , 40, (25,0,51))
	label_mouhammed.draw()
	onScreen.append(label_mouhammed)

	label_itay = UIClasses.Label(main_screen, background_color, "Itay", 150, 400 , 40, (25,0,51))
	label_itay.draw()
	onScreen.append(label_itay)


	
#Initialize everythings before starting to work with the UI. MUST BE CALLED AT THE BEGGINIG OF THE PROGRAM
def initialize():
	global onScreen		
	global main_screen
	global background_color
	
	global emotionsDict
	global PUDict
	global cart
	global currentScreen
	global PUButtons
	global 	emotionButtons

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
	currentScreen = "main"
	PUButtons = []
	emotionButtons = []
	
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
				currentScreen = "emotionsScreen"

			if button_PU.visible and button_PU.click(x,y):
				clearScreen()
				PUScreen()
				currentScreen = "PUScreen"

			if button_back.visible and button_back.click(x, y):
				if(currentScreen == "viewProductScreen"):
					main_screen.fill(background_color)
					counterLabel.draw()					
				clearScreen()
				currentScreen = "main"
				mainScreen()
			if button_Cart.visible and button_Cart.click(x, y):
				clearScreen()
				cartScreen()
				currentScreen = "cartScreen"
			if button_addToCart.visible and button_addToCart.click(x, y):
				if(counterLabel.text != "0"):
					cart.append(dafClasses.cartProduct(currentProduct, int(counterLabel.text)))
					clearScreen()
					main_screen.fill(background_color)
					cartScreen()
					currentScreen = "cartScreen"
			if button_plus.visible and button_plus.click(x, y):
				newValue = int(counterLabel.text) + 1
				counterLabel.text = str(newValue);
				counterLabel.draw()
			if button_minus.visible and button_minus.click(x, y):
				newValue = int(counterLabel.text) - 1
				if newValue >= 0:
					counterLabel.text = str(newValue);

					counterLabel.draw()
			if currentScreen == "emotionsScreen":
				for button in emotionButtons:
					if(button.click(x, y)):
						clearScreen()
						currentScreen = "viewProductScreen"
						counterLabel.text = "0"
						viewProductScreen(emotionsDict[button.text])
			if currentScreen == "PUScreen":
				for button in PUButtons:
					if(button.click(x, y)):
						clearScreen()
						currentScreen = "viewProductScreen"
						counterLabel.text = "0"
						viewProductScreen(PUDict[button.text])
			if currentScreen == "cartScreen" and button_buy.click(x, y):
				clearScreen()
				currentScreen = "thankYouScreen"
				thankYouScreen()
				
		pygame.display.flip()
