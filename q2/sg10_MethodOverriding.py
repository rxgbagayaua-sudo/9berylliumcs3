class Animal:
    def __init__(self,name:str):
        self.name = name

    def make_sound():
        print(f"{self.name} makes a sound")
    def eat():
        print(f"{self.name} eats")
    
class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars loudly!")
    def eat(self):
        print(f"{self.name} eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")
    def eat(self):
        print(f"{self.name} eats Grass and Fruit.")
        
class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")
    def eat(self):
        print(f"{self.name} eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")
print("==========OUTPUT==========")
print("==========================")
lion.make_sound()
lion.eat()

print("==========================")
elephant.make_sound()
elephant.eat()

print("==========================")
monkey.make_sound()
monkey.eat()