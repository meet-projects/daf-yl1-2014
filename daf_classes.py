class product(object):
	def __init__(self,price ,duration, bottle_size, color):
		self.price = price
		self.duration = duration
		self.bottle_size = bottle_size
		self.color= color

class emotion(product):
	def __init__(self, price, duration, bottle_size, color, flavour):
		super(emotion, self).__init__(price, duration, bottle_size, color)
 		self.flavour = flavour

class powerup(product):
	def __init__(self, price, duration, bottle_size , color, brand ):
		super(powerup, self).__init__(price, duration, bottle_size,color )
 		self.brand = brand


angry=("50", "60", "Medium", "Red", "Orange")
print "Emotion"
print "price: " + angry.price + "NIS."
print "duration: " + angry.duration + "Minutes."
print "color: " + angry.color
print "bottle size: " + angry.bottle_size
print "flavour: " + angry.flavour

anxious=("75", "90", "Large", "Blue", "Cherry")
print "Emotion"
print "price: " + anxious.price + "NIS."
print "duration: " + anxious.duration + "Minutes."
print "color: " + anxious.color
print "bottle size: " + anxious.bottle_size
print "flavour: " + anxious.flavour

frustrated=("65", "60", "Medium", "Purple", "Lime")
print "Emotion"
print "price: " + frustrated.price + "NIS."
print "duration: " + frustrated.duration + "Minutes."
print "color: " + frustrated.color
print "bottle size: " + frustrated.bottle_size
print "flavour: " + frustrated.flavour

annoyed=("89", "120", "Large", "Pink", "Fruit Punch")
print "Emotion"
print "price: " + annoyed.price + "NIS."
print "duration: " + annoyed.duration + "Minutes."
print "color: " + annoyed.color
print "bottle size: " + annoyed.bottle_size
print "flavour: " + annoyed.flavour

isolated=("50", "45", "Medium", "Dark Red", "Raspberry")
print "Emotion"
print "price: " + isolated.price + "NIS."
print "duration: " + isolated.duration + "Minutes."
print "color: " + isolated.color
print "bottle size: " + isolated.bottle_size
print "flavour: " + isolated.flavour

panicked=("53", "60", "Medium", "Orange", "Peach")
print "Emotion"
print "price: " + panicked.price + "NIS."
print "duration: " + panicked.duration + "Minutes."
print "color: " + panicked.color
print "bottle size: " + panicked.bottle_size
print "flavour: " + panicked.flavour

shocked=("85", "90", "Large", "Maroon", "Strawberry")
print "Emotion"
print "price: " + shocked.price + "NIS."
print "duration: " + shocked.duration + "Minutes."
print "color: " + shocked.color
print "bottle size: " + shocked.bottle_size
print "flavour: " + shocked.flavour

disappointed=("100", "120", "Large", "Lavender", "Lemonade")
print "Emotion"
print "price: " + disappointed.price + "NIS."
print "duration: " + disappointed.duration + "Minutes."
print "color: " + disappointed.color
print "bottle size: " + disappointed.bottle_size
print "flavour: " + disappointed.flavour

abandoned=("95", "90", "Large", "Yellow", "Green Tea")
print "Emotion"
print "price: " + abandoned.price + "NIS."
print "duration: " + abandoned.duration + "Minutes."
print "color: " + anbandoned.color
print "bottle size: " + abandoned.bottle_size
print "flavour: " + abadoned.flavour

hurt=("59", "60", "Medium", "Light Blue", "Pineapple")
print "Emotion"
print "price: " + hurt.price + "NIS."
print "duration: " + hurt.duration + "Minutes."
print "color: " + hurt.color
print "bottle size: " + hurt.bottle_size
print "flavour: " + hurt.flavour

sad=("102", "120", "Large", "Green", "Apple")
print "Emotion"
print "price: " + sad.price + "NIS."
print "duration: " + sad.duration + "Minutes."
print "color: " + sad.color
print "bottle size: " + sad.bottle_size
print "flavour: " + sad.flavour

rejected=("76", "90", "Large", "Blue", "Pink Grapefruit")
print "Emotion"
print "price: " + rejected.price + "NIS."
print "duration: " + rejected.duration + "Minutes."
print "color: " + rejected.color
print "bottle size: " + rejected.bottle_size
print "flavour: " + rejected.flavour

worried=("95", "120", "Large", "Red", "Pear")
print "Emotion"
print "price: " + worried.price + "NIS."
print "duration: " + worried.duration + "Minutes."
print "color: " + worried.color
print "bottle size: " + worried.bottle_size
print "flavour: " + worried.flavour

bored=("68", "90", "Medium", "Green", "Mango")
print "Emotion"
print "price: " + bored.price + "NIS."
print "duration: " + bored.duration + "Minutes."
print "color: " + bored.color
print "bottle size: " + bored.bottle_size
print "flavour: " + bored.flavour

lonely=("64", "90", "Medium", "Orange", "Tropical Punch")
print "Emotion"
print "price: " + lonely.price + "NIS."
print "duration: " + lonely.duration + "Minutes."
print "color: " + lonely.color
print "bottle size: " + lonely.bottle_size
print "flavour: " + lonely.flavour

depressed=("78", "60", "Large", "Violet", "Grape")
print "Emotion"
print "price: " + depressed.price + "NIS."
print "duration: " + depressed.duration + "Minutes."
print "color: " + depressed.color
print "bottle size: " + depressed.bottle_size
print "flavour: " + depressed.flavour


sleepy = powerup("120", "150", "Large", "Yellow", "RedBull")
print "Power Up"
print "price: " + sleepy.price + "NIS."
print "duration: " + sleepy.duration + "Minutes."
print "bottle size: " + sleepy.bottle_size
print "color: " + sleepy.color
print "brand: " + sleepy.brand

lazy = powerup("75", "60", "Medium", "Blue", "XL")
print "Power Up"
print "price: " + lazy.price + "NIS."
print "duration: " + lazy.duration + "Minutes."
print "bottle size: " + lazy.bottle_size
print "color: " + lazy.color
print "brand: " + lazy.brand

exhausted = powerup("95", "120", "Large", "Green", "Monster")
print "Power Up"
print "price: " + exhausted.price + "NIS."
print "duration: " + exhausted.duration + "Minutes."
print "bottle size: " + exhausted.bottle_size
print "color: " + exhausted.color
print "brand: " + exhausted.brand

fatigued = powerup("83", "75", "Medium", "Purple", "Blue")
print "Power Up"
print "price: " + fatigued.price + "NIS."
print "duration: " + fatigued.duration + "Minutes."
print "bottle size: " + fatigued.bottle_size
print "color: " + fatigued.color
print "brand: " + fatigued.brand

weak = powerup("105", "90", "Large", "Red", "Sparks")
print "Power Up"
print "price: " + weak.price + "NIS."
print "duration: " + weak.duration + "Minutes."
print "bottle size: " + weak.bottle_size
print "color: " + weak.color
print "brand: " + weak.brand



