#Create Classes
class Car:
    def __init__(self, name, model, power, price):
        self.name = name
        self.model = model
        self.power = power
        self.price = price


class CarShowRoom:
    def __init__(self):
        self.cars = []