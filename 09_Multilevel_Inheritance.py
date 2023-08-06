class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks.")

class Labrador(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color

    def fetch(self):
        print(f"{self.name} fetches.")

dog = Labrador("Buddy", "Labrador Retriever", "Golden")
dog.speak()
dog.bark()
dog.fetch()
print(dog.color)
print(dog.breed)
print(dog.name)