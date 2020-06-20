from vehicle import Vehicle


class Fiat(Vehicle):
    def __init__(self, color):
        self.fuel = 0
        self.main_color = color

    def drive(self):
        print(f"The {self.main_color} Fiat goes scooooooot!")

    def refuel(self):
        self.fuel = 100
        print("The Fiat's fuel tank is now full!")

    def turn(self, direction):
        print(f"The Fiat scoots to the {direction}")

    def stop(self):
        print("The Fiat squeaks to a stop")