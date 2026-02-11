class Plant:
    """
    Represents a plant with a name and height

    Attributes
    ----------
    name : str
        The name of the plant.
    height : int
        The height of the plant in centimeters.
    """

    def __init__(self, name: str, height: int) -> None:
        """
        Initialize the plant with name and height.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in cm.
        """
        self.name: str = name
        self.height: int = height
    
    def grow(self, growValue : int):
        self.height += growValue
        print(f"{self.name} grew {growValue}cm")

    


class FloweringPlant(Plant):
    
    def __init__(self, name : str, height : int, color : str) -> None:
        super().__init__(name, height)
        self.color : str = color



class PrizeFlower(FloweringPlant):

    def __init__(self, name : str, height : int, color : str, prize_point : int) -> None:
        super().__init__(name, height, color)
        self.prize_point : int = prize_point


class Garden:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants: list[Plant | FloweringPlant | PrizeFlower] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name.capitalize()} to {self.name}'s garden")

    def display_garden(self) -> None:
        for plant in self.garden:
            print(f"{plant}")

    def help_plant(self, growValue : int) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(growValue)

    def garden_report(self):
        print(f"=== {self.name.capitalize()}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.name.capitalize()}: {plant.height}cm")


class GardenManager:

    gardens : list[Garden] = []
    handleGardens : int = 0

    class GardenStats:

        def __init__(self, plants : list[Plant]):
            self.plants = plants
        
        def plant_type(self) -> dict[str, int]:
            types_count : dict[str, int] = {"regular": 0, "flowering": 0, "Prize": 0}
            for plant in self.plants:
                if isinstance(plant, Plant):
                    types_count["regular"] += 1
                if isinstance(plant, FloweringPlant):
                    types_count["flowering"] += 1
                else:
                    types_count["prize"] += 1
            return types_count

    @staticmethod
    def stats_display(self):
        ...

    @classmethod
    def create_garden_network(cls, gardenList : list[Garden]):
        for garden in gardenList:
            cls.handleGardens += 1
            cls.gardens.append(garden)


def main() -> None:
    print("=== Garden Management System Demo ===")
    print()
    alice = Garden("Alice")
    alice.add_plant(Plant("oak tree", 100))
    alice.add_plant(FloweringPlant("rose", 25, "red"))
    alice.add_plant(PrizeFlower("sunflower", 50, "yellow", 10))
    print()
    alice.help_plant(1)
    print()
    alice.garden_report()


if __name__ == "__main__":
    main()
