from oop_inheritance import Mammal

class LandMammal(Mammal):
    pass


if __name__ == '__main__': 
    monkey = LandMammal('monkey', 2)
    monkey.breathing()