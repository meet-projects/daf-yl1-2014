class emotion(product):
    def __init__(self,price ,duration, flavour):
        self.price = 
        self.duration = 
        self.flavour = 
    
class powerup(product):
    def __init__(self,price ,duration, flavour):
        self.price = 
        self.duration = 
        self.flavour = 

if __name__=="__main__":
    m = product("100","30", "mango")
    print m.price
    print m.letter_grade()
    
    n = UniversityStudent("Kyle Hannon", 2013, "MIT")
    print n.name
    print n.score
    print n.year
    print n.signature()
