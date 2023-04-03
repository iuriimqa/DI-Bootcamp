Daily

class Farm:

    def __init__(self, name: str) -> None:
        self.name = name
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount

    def get_info(self) -> str:
        farm_name_cap = self.name.capitalize()
        animal_farm_str = f"{farm_name_cap}'s farm\n"
        eieio_str = '    E-I-E-I-0!'

        animals_str = ""
        for animal, amount in self.animals.items():
            animals_str += f"{animal} : {amount}\n"

        info = animal_farm_str + '\n' + animals_str + '\n' + eieio_str
        return info

    def get_animal_types(self) -> str:
        animal_names = self.animals.keys()
        animal_names_sorted = sorted(animal_names)
        return animal_names_sorted

    def get_short_info(self) -> str:
        animal_types = self.get_animal_types()
        farm_name_cap = self.name.capitalize()
        farm_name = f"{farm_name_cap} farm has "

        animals_str = ""
        for i, animal in enumerate(animal_types):
            if i == len(animal_types) - 2:
                animals_str += f"{animal} and "
            elif i == len(animal_types) - 1:
                animals_str += f"{animal}."
            else:
                animals_str += f"{animal}, "

        repr = farm_name + animals_str
        return repr
    # McDonald’s farm has cows, goats and sheep.


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print(macdonald.get_animal_types())
print(macdonald.get_short_info())