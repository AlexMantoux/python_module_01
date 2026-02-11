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


class FloweringPlant(Plant):
    pass


class PriweFlower(FloweringPlant):
    pass


class Garden:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.garden: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.garden.append(plant)
        print(f"Added {plant.name.capitalize()} to {self.name}'s garden")

    def display_garden(self):
        for plant in self.garden:
            print(f"{plant}")


class GardenManager:
    pass


def main() -> None:
    print("=== Garden Management System Demo ===")
    print()
    alice = Garden("Alice")
    alice.add_plant(Plant("oak tree", 25))
    alice.add_plant(Plant("rose", 25))
    alice.add_plant(Plant("sunflower", 25))


if __name__ == "__main__":
    main()
