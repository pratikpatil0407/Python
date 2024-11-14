class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    def speak(self):  #method overriding
        return f"{self.name} meows"
    
cat = Cat("Whiskers")

print(cat.speak())