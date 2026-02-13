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
            height (int): The height of the plant in cm.
            age (int): The age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age
        print(f"Created: {self.name.capitalize()} ({self.height}cm, "
              f"{self.age} days)")


class PlantFactory:
    """
    A class to represent factory for create plant.
    """
    factoryPlant: int = 0

    def create_plant(val: tuple[str, int, int]) -> Plant:
        """
        Create lot of plants

        Args:
            val tuple[str, int, int]: Table of values
        """
        PlantFactory.factoryPlant += 1
        name: str
        height: int
        age: int
        name, height, age = val
        return Plant(name, height, age)


if __name__ == "__main__":
    plants_tuple = [
            ("rose", 25, 30),
            ("oak", 200, 365),
            ("cactus", 5, 90),
            ("sunflower", 80, 45),
            ("fern", 15, 120)
        ]

    print("=== Plant Factory Output ===")

    plants: Plant = []
    for plant in plants_tuple:
        plants.append(PlantFactory.create_plant(plant))
    print()
    print(f"Total plants created: {PlantFactory.factoryPlant}")
