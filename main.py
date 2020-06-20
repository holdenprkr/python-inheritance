from acura import Acura
from fiat import Fiat
from jeep import Jeep
from lamborghini import Lamborghini
from tesla import Tesla

acura = Acura("gray")
fiat = Fiat("golden")
jeep = Jeep("red")
lamborghini = Lamborghini("yellow")
tesla = Tesla("blue")

acura.drive()
acura.turn("right")
acura.stop()
print()
fiat.drive()
fiat.turn("left")
fiat.stop()
print()
jeep.drive()
jeep.turn("right")
jeep.stop()
print()
lamborghini.drive()
lamborghini.turn("left")
lamborghini.stop()
print()
tesla.drive()
tesla.turn("right")
tesla.stop()
