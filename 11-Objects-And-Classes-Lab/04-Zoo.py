class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammals":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        if species == "mammal":
            species_names = self.mammals
        if species == "fishe":
            species_names = self.fishes
        if species == "bird":
            species_names = self.birds
        names = ", ".join(species_names)
        return f"{species} in {zoo_name}: {names}"

    def get_total(self):
        return f"Total animals: {self.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animals(species, name)

species = input()
print(zoo.get_info(species))
print(zoo.get_total())