from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def calc (self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    def calc(self, V):
        return round((V/6.5 + 0.5), 1)

    def __str__(self):
        return f'Расход ткани на пальто - {self.calc(self.V)} метров'

class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    def calc(self, H):
        return round((2*H/100 + 0.3), 1)

    def __str__(self):
        return f'Расход ткани на костюм - {self.calc(self.H)} метров'


coat_1 = Coat(50)
print(str(coat_1))
suit_1 = Suit(175)
print(str(suit_1))
print(f'Расход ткани на пальто и костюм {coat_1.calc(coat_1.V) + suit_1.calc(suit_1.H)} метров')