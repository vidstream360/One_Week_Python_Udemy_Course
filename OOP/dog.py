#a class is a blueprint for objects that says what objects have in terms of attributes + functionality
#attributes are variables / data 
#methods add functionality
#first parameter for def is self
#first will refer to an instance of the class

class Dog:
    def __init__(self, name, breed, location):  # class with attributes
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    species = 'canine' #can add non instance attributes this way

    @classmethod             #class methods executed on the class themselves, not instances
    def register_stray(cls): 
        return cls('coming soon', 'unknow', 'unkown')
    
    def bark(self):
        print(f"{self.name} says WOOF!")         #methods act on instances

    def eat(self):
        print("NOM NOM!")

    def learn_trick(self,new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def perfrom_trick(self, trick):     
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} does not know {trick}")

elton = Dog('elton', 'australian sheperd', 97236)
elton.learn_trick('sit')
elton.learn_trick('stay')

jimbo = Dog('jimbo', 'mutt', 97236)
jimbo.learn_trick('sit')
jimbo.learn_trick('stay')


