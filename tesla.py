from vehicle import Vehicle


class Tesla(Vehicle):
    def __init__(self, color):
        self.battery_kwh = 0
        self.main_color = color

    def drive(self):
        print(f"The {self.main_color} Tesla goes zoooooooooooom!")

    def charge_battery(self):
        self.battery_kwh = 100
        print("The Tesla's battery is now charged!")

    def turn(self, direction):
        print(f"The Tesla zooms to the {direction}")

    def stop(self):
        print("The Tesla quietly but quickly comes to a stop")