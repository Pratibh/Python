__author__ = 'pratibh'

# Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print "Speak"


class Dog(Animal):
    def speak(self):
        print "Bark"


class Cat(Animal):
    def speak(self):
        print "Meow"


dog = Dog("Dog")
dog.speak()

cat = Cat("Cat")
cat.speak()
