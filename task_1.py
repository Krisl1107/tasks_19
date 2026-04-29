class Dog:
    """
    Dog class represents a dog with a name.

    Methods:
        say() - prints the phrase "Гав!"
    """
    def __init__(self, name):
        self.name = name

    def say(self):
        print("Гав!")


small_dog = Dog("Teddy")
print(small_dog.name)
small_dog.say()
print("The dog's name is", small_dog.name)
