class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def rotate(self):
        return "Wheels are rotating"

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        return "Engine started"

class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def open(self):
        return "Doors opened"

class Car(Wheels, Engine, Doors):
    def __init__(self, brand, model, fuel_type, number_of_wheels, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, fuel_type)
        Doors.__init__(self, number_of_doors)
        self.brand = brand
        self.model = model

    def drive(self):
        return "Car is driving"

if __name__ == "__main__":
    car = Car(brand="Porsche", model="911 Dakar", fuel_type="Gasoline", number_of_wheels=4, number_of_doors=4)
    print(car.drive())
    print(car.rotate())
    print(car.start())
    print(car.open())
