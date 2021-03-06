from vehicle import Vehicle


class Lamborghini(Vehicle):
    def __init__(self, color):
        self.fuel = 0
        self.main_color = color

    def drive(self):
        print(f"The {self.main_color} Lamborghini goes skrrrrrrrrrr!")

    def refuel(self):
        self.fuel = 100
        print("The Lamborghini's fuel tank is now full!")

    def turn(self, direction):
        print(f"The Lamborghini skrrrts to the {direction}")

    def stop(self):
        print("The Lamborghini comes to a stop quicker than you can say it")
        
