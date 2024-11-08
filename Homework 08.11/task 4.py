class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"


class CarShop:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)


    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"The car {car} has been sold.")
        else:
            print("The car is not available in the shop.")

    def __str__(self):
        if self.cars:
            cars_info = "\n".join(map(str, self.cars))
            return f"Cars available for sale:\n{cars_info}"
        else:
            return "No cars available for sale."


car1 = Car("Toyota", "Camry", 2020, 20000)
car2 = Car("Honda", "Civic", 2019, 18000)
car3 = Car("Ford", "Mustang", 2021, 30000)

car_shop = CarShop()
car_shop.add_car(car1)
car_shop.add_car(car2)
car_shop.add_car(car3)

print(car_shop)

car_shop.sell_car(car2)

print(car_shop)
