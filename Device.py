class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model}"

class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

    def make_coffee(self):
        return f"Making {self.coffee_type} coffee with {self.get_info()}"

class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels

    def blend(self, ingredient):
        return f"Blending {ingredient} with {self.get_info()} at {self.speed_levels} speed levels"

class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self, meat_type):
        return f"Grinding {meat_type} with {self.get_info()} at {self.power} watts"



if __name__ == "__main__":
    coffee_machine = CoffeeMachine("BrandA", "ModelX", "Espresso")
    print(coffee_machine.make_coffee())

    blender = Blender("BrandB", "ModelY", 3)
    print(blender.blend("Fruits"))

    meat_grinder = MeatGrinder("BrandC", "ModelZ", 800)
    print(meat_grinder.grind_meat("Beef"))
