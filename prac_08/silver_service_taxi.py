from prac_08 import Taxi


flagfall = 4.5


def init(self, name, fuel, fanciness):
    super().__init__(name, fuel)
    self.fanciness = fanciness
    self.price_per_km *= fanciness




