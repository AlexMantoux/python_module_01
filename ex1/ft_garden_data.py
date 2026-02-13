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

    def display(self) -> None:
        """
        Display basic information about plant.
        """
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


if __name__ == "__main__":

    plants: list[Plant] = [
        Plant("rose", 25, 30),
        Plant("sunFlower", 80, 45),
        Plant("cactus", 15, 120)
        ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display()
