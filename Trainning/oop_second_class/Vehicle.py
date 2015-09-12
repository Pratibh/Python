__author__ = 'pratibh'


class Vehicle:
    type_of_vehicle = ""
    price_of_vehicle = ""
    color_of_vehicle = ""

    def __init__(self, type, price, color):
        self.type_of_vehicle = type
        self.price_of_vehicle = price
        self.color_of_vehicle = color

    def setModel(self, model):
        self.model_of_vehicle = model

    def setHorsepower(self, horsepower):
        self.horse_power = horsepower

    def getModel(self):
        return self.model_of_vehicle

    def getHorsepower(self):
        return self.horse_power

Lambo = Vehicle("SUV","$200000","Yellow")
Lambo.setModel("Urus")
Lambo.setHorsepower("100000")

print Lambo.type_of_vehicle
print Lambo.price_of_vehicle
print Lambo.color_of_vehicle
print Lambo.getModel()
print Lambo.getHorsepower()
print Lambo.color_of_vehicle


