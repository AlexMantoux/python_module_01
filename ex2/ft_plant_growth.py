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
        self.age_days: int = age

    def get_info(self) -> None:
        """
        Display basic information about plant.
        """
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age_days} days old")

    def grow(self) -> None:
        """
        Increase the plant's height by 1.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increase the plant's age by 1.
        """
        self.age_days += 1


if __name__ == "__main__":
    days: int = 6
    rose: Plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    for _ in range(days):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{days}cm")
