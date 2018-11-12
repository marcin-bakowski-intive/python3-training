
class Vehicle:
    car_type = None

    def __init__(self, color, price, car_type=None):
        self.color = color
        self.price = price
        self.car_type = car_type or self.car_type

    def __str__(self):
        return "<Vehicle type=%s color=%s price=%s>" % (self.car_type, self.color, self.price)


class SUV(Vehicle):
    car_type = "SUV"


class Cabrio(Vehicle):
    car_type = "Cabrio"


class Sedan(Vehicle):
    car_type = "Sedan"


class Garage:
    def __init__(self):
        self.cars = []

    def park(self, car):
        self.cars.append(car)

    def leave(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def __str__(self):
        return "<Garage with %s cars>" % ", ".join(str(car) for car in self.cars)


suv = SUV("Black", 1000)
cabrio = Cabrio("Red", 2000)
garage = Garage()
garage.park(suv)
garage.park(cabrio)
print(garage)

garage.leave(suv)
print(garage)
