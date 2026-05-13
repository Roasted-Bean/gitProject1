class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says ..."

    def __str__(self):
        return f"{self.name} (age {self.age})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says Meow!"

    def status(self):
        location = "indoor" if self.indoor else "outdoor"
        return f"{self.name} is an {location} cat."


if __name__ == "__main__":
    dog = Dog("Rex", 3, "Labrador")
    cat = Cat("Nabi", 5, indoor=True)

    for animal in [dog, cat]:
        print(animal)
        print(animal.speak())

    print(dog.fetch("ball"))
    print(cat.status())
