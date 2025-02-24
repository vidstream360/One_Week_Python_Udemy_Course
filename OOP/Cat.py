#inheritance

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows!!!!")


c = Cat('blue')
print(c.name)
print(c.meow())

class Cougar(Cat):               #class cougar inherits its attributes from class cat this way
    def purr(self):              #if no init method it calls it from mother class
        print(f"{self.name} purrrs")

puma = Cougar('tina')

print(puma.name)
print(puma.purr())

class Lion(Cat):
    def roar(self):
        print(f"{self.name} roars")

lion = Lion('eli')

print(lion.name)
print(lion.roar())

class Tiger(Cat):
    def __init__(self, name, pride_name):
        print("INSIDE TIGER INIT")
        super().__init__(name)     #super makes python find the super class, in this case cat
        self.pride_name = pride_name
    def roar(self):
        print(f"{self.name} roars")
