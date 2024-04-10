class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def get_info(self):
        return f"{self.name} - Displacement: {self.displacement} tons"

class Frigate(Ship):
    def __init__(self, name, displacement, missile_system):
        super().__init__(name, displacement)
        self.missile_system = missile_system

    def launch_missile(self):
        return f"Launching missiles from {self.missile_system} on {self.get_info()}"

class Destroyer(Ship):
    def __init__(self, name, displacement, artillery_guns):
        super().__init__(name, displacement)
        self.artillery_guns = artillery_guns

    def fire_artillery(self):
        return f"Firing artillery guns on {self.get_info()}"

class Cruiser(Ship):
    def __init__(self, name, displacement, radar_system):
        super().__init__(name, displacement)
        self.radar_system = radar_system

    def operate_radar(self):
        return f"Operating radar system on {self.get_info()}"

if __name__ == "__main__":
    frigate_ship = Frigate("FrigateA", 2000, "Aegis")
    print(frigate_ship.launch_missile())

    destroyer_ship = Destroyer("DestroyerX", 3500, "5-inch guns")
    print(destroyer_ship.fire_artillery())

    cruiser_ship = Cruiser("CruiserZ", 5000, "Phased Array Radar")
    print(cruiser_ship.operate_radar())
