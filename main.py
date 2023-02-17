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





    #Add Function
    def add(self, name, model, power, price):
        car = Car(name, price, model, power)
        self.cars.append(car)
        print(f"{name} Added")


