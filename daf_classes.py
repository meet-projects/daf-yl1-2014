#Leen&AseelR
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
    

e = emotion("100", "50", "large", "red", "orange")
print "Emotion"
print "price: " + e.price
print "duration: " + e.duration
print "color: " + e.color
print "bottle size: " + e.bottle_size
print "flavour: " + e.flavour

p = powerup("120", "30", "medium", "blue", "RedBull")
print "Power Up"
print "price: " + p.price
print "duration: " + p.duration
print "bottle size: " + p.bottle_size
print "color: " + p.color
print "brand: " + p.brand
