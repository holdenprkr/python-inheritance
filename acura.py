from vehicle import Vehicle


class Acura(Vehicle):
    def __init__(self, color):
        self.fuel = 0
        self.main_color = color

    def drive(self):
        print(f"The {self.main_color} Acura goes weeooooooooooooooow!")

    def refuel(self):
        self.fuel = 100
        print("The Acura's fuel tank is now full!")

    def turn(self, direction):
        print(f"The Acura drifts to the {direction}")

    def stop(self):
        print("The Acura slams to a stop")
