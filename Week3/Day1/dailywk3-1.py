class Farm:
    def __init__(self,farm:str) -> None:
         self.farm = farm
         self.animals ={}


    def add_animal(self,animal_type,amount = 1):
         if animals in self.animals:
             self.animals[animal] += amount
         else:
             self.animals[animal] = amount
    def get_info(self) -> str:
        fam_name_cap = self.name.capitalize()
        animal_farm_str =
# cow = Farm('cow',5)
# sheep = Farm('sheep',2)
# goat = Farm('goat',12)

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep',1)
macdonald.add_animal('sheep',1)
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.animals)
