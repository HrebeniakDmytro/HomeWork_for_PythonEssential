class Car:
    def __init__(self, make, model, year, fuel_capacity):
        self.make = make                
        self.model = model              
        self.year = year                
        
        self.__mileage = 0          
        self.__fuel_level = 0          
        self.__fuel_capacity = fuel_capacity 

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage >= self.__mileage:
            self.__mileage = mileage
        else:
            print("Новий пробіг не може бути меншим за поточний!")

    def get_fuel_level(self):
        return self.__fuel_level

    def refuel(self, liters):
        if liters > 0:
            if self.__fuel_level + liters <= self.__fuel_capacity:
                self.__fuel_level += liters
            else:
                print("Не можна заправити більше, ніж вміщує бак!")
        else:
            print("Кількість літрів для заправки повинна бути додатньою!")

    def drive(self, distance, consumption_per_km):
        required_fuel = distance * consumption_per_km
        if required_fuel <= self.__fuel_level:
            self.__fuel_level -= required_fuel
            self.__mileage += distance
        else:
            print("Недостатньо палива для поїздки!")

my_car = Car("Toyota", "Corolla", 2020, 50)
my_car.set_mileage(10000)
print(f"Пробіг автомобіля: {my_car.get_mileage()} км")

my_car.refuel(20)
print(f"Рівень палива: {my_car.get_fuel_level()} літрів")

my_car.drive(50, 0.5)
print(f"Пробіг автомобіля після поїздки: {my_car.get_mileage()} км")
print(f"Рівень палива після поїздки: {my_car.get_fuel_level()} літрів")
