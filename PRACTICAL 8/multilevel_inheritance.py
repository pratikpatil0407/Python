class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def walk(self):
        print(f"{self.name} is walking.")

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name}, the {self.breed} is barking.")

my_dog = Dog("Max", 3, "Golden Retriever")

my_dog.eat()
my_dog.walk()
my_dog.bark()