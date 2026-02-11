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
        self.total_growth = 0

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
            self.total_growth += growValue

    def garden_report(self):
        print(f"=== {self.name.capitalize()}'s Garden Report ===")
        print("Plants in garden:")
        
        for plant in self.plants:
            line = f"- {plant.name.capitalize()}: {plant.height}cm"
            if isinstance(plant, FloweringPlant):
                line += f", {plant.color} flowers (blooming)"
            if isinstance(plant, PrizeFlower):
                line += f", Prize points: {plant.prize_point}"
            print(line)
        stats = GardenManager.GardenStats(self)
        types = stats.plant_type()
        print()
        print(f"Plants added: {len(self.plants)}, Total growth: {self.total_growth}cm")
        print(f"Plant types: {types['regular']} regular, {types['flowering']} flowering, {types['prize']} prize flowers")
        print()

class GardenManager:

    gardens : list[Garden] = []
    handleGardens : int = 0

    class GardenStats:

        def __init__(self, garden : Garden):
            self.garden = garden
            self.plants = garden.plants
        
        def plant_type(self) -> dict[str, int]:
            types_count : dict[str, int] = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    types_count["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    types_count["flowering"] += 1
                else:
                    types_count["regular"] += 1
            return types_count
        
        def total_plants(self) -> int:
            return len(self.plants)
        
        def total_growth(self) -> int:
            return self.garden.total_growth
                
        def calculate_score(self) -> int:
            score = 0
            for plant in self.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_point
            score += len(self.plants) * 10
            return score

    def stats_display(self):
        ...

    @staticmethod
    def validate_heights() -> bool:
        for garden in GardenManager.gardens:
            for plant in garden.plants:
                if plant.height <= 0:
                    return False
        return True
    
    @classmethod
    def stats_display(cls):
        print(f"Height validation test: {cls.validate_heights()}")
        print("Garden scores - ", end="")
        scores = []
        for garden in cls.gardens:
            stats = cls.GardenStats(garden)
            score = stats.calculate_score()
            scores.append(f"{garden.name.capitalize()}: {score}")
        print(", ".join(scores))
        print(f"Total gardens managed: {cls.handleGardens}")

    @classmethod
    def create_garden_network(cls, gardenList : list[Garden]):
        for garden in gardenList:
            cls.handleGardens += 1
            cls.gardens.append(garden)


def main() -> None:

    bob = Garden("Bob")
    alice = Garden("Alice")
    GardenManager.create_garden_network([alice, bob])
    print("=== Garden Management System Demo ===")
    print()
    alice.add_plant(Plant("oak tree", 100))
    alice.add_plant(FloweringPlant("rose", 25, "red"))
    alice.add_plant(PrizeFlower("sunflower", 50, "yellow", 10))
    print()
    alice.help_plant(1)
    print()
    alice.garden_report()
    GardenManager.stats_display()

if __name__ == "__main__":
    main()
