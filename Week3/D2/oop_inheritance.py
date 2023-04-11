class Animal: #parent

    def __init__(self, name: str):
        self.name = name

    def breathing(self):
        out = f'{self.name} breaths'
        print(out) 

class Mammal(Animal): #child

    def __init__(self, name: str, lungs: int):
        super().__init__(name)
        print(type(self))
        self.lungs = lungs
    
    def produce_milk(self):
        out = f'{self.name} produces milk'
        print(out)


class SeaMammal(Mammal):
    
    def __init__(self, name: str, lungs: int):
        super().__init__(name, lungs)
        self.fins = True

    def hold_breath(self):
        out = f'{self.name} holds breath'
        print(out)



if __name__ == '__main__': # tells python what to run when running script directly
    m = Mammal('m', 2)
    dolphin = SeaMammal('dolphin', 2)
