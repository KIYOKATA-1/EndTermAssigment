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
        print(f"{name} 𝗗𝗢𝗡𝗘 ✔")


    #Update Function
    def Update(self , index, name=None, price=None, model=None, power=None):
        car = self.cars[index - 1]
        if name:
            car.name = name
        if model:
            car.model = model
        if power:
            car.power = power
        if price:
            car.price = price
        print(f"{car.name} ~𝐔𝐃𝐀𝐓𝐄𝐃~ ")

    #Delete Funcrion
    def delete(self, index):
        car = self.cars.pop(index - 1)
        print(f"{car.name} 𝑹𝑬𝑴𝑶𝑽𝑬𝑫 ")
