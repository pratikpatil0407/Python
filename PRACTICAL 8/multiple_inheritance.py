class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name}, the {self.breed}, barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())