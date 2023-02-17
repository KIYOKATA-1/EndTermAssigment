#Create Classes/Сыныптар құру:
class Car:
    def __init__(self, name, model, power, price):
        self.name = name
        self.model = model
        self.power = power
        self.price = price


class CarShowRoom:
    def __init__(self):
        self.cars = []


    #Add Function/Функция қосу:
    def add(self, name, model, power, price):
        car = Car(name, price, model, power)
        self.cars.append(car)
        print(f"{name} 𝗗𝗢𝗡𝗘 ✔")


    #Update Function/Жаңарту функциясы:
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


    #Delete Funcrion/Функцияны Жою:
    def delete(self, index):
        car = self.cars.pop(index - 1)
        print(f"{car.name} 𝑹𝑬𝑴𝑶𝑽𝑬𝑫 ")


    #Create Menu/Мәзір жасау:

showroom = CarShowRoom()
while True:
    print("\n~~~~~~~~ＭＥＮＵ~~~~~~~~")
    print("[1] ~ 🄰🄳🄳 🄲🄰🅁")
    print("[2] ~ 🅁🄴🄰🄳")
    print("[3] ~ 🅄🄿🄳🄰🅃🄴")
    print("[4] ~ 🄳🄴🄻🄴🅃🄴")
    print("[5] ~ 🄴🅇🄸🅃")

    choice = int(input("▼▼▼▼▼▼▼𝐂𝐇𝐎𝐎𝐒𝐄 𝐓𝐇𝐄 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍▼▼▼▼▼▼▼\n"))

    if choice == 1:
        name = input("Input Name of Car ~> ")
        model = input("Input Model of Car ~> ")
        power = input("Input Power ~> ")
        price = input("Input Price ~> ")
        showroom.add(name, model, power, price)

    elif choice == 2:
        showroom.read()

    elif choice == 3:
        index = int(input("Enter car index to update: "))
        name = input("Enter new make (press enter to keep existing value): ")
        model = input("Enter new model (press enter to keep existing value): ")
        power = input("Enter new year (press enter to keep existing value): ")
        price = input("Enter new price (press enter to keep existing value): ")
        showroom.update_car(index, name, model, power, price)

    elif choice == 4:
        index = int(input(f"Input Car Index For Delete"))
        showroom.delete(index)

    elif choice == 5:
        break;

    else:
        print("INVALID SYNTAX")