class Plant:
    """
    Represents a plant with a name, height, and age.

    Attributes
    ----------
    name : str
        The name of the plant.
    height : int
        The height of the plant in centimeters.
    age : int
        The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the plant with name, age, and height.

        Args:
            name (str): The name of the plant.
            age (int): The age of the plant in days.
            height (int): The height of the plant in cm.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


def display_plant(plant: Plant) -> None:
    """
    Display basic information about a plant.

    Parameters
    ----------
    plant : Plant
        The Plant object to display.
    """
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    display_plant(Plant("Rose", 25, 30))
    display_plant(Plant("SunFlower", 80, 45))
    display_plant(Plant("Cactus", 15, 120))
