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
        self.last_height: int = height
        self.last_age_days: int = age
        print(f"Created: {self.name} ({self.height}cm, {self.age_days} days)")

    def display(self) -> None:
        """
        Display the plant's details.
        """
        print(f"{self.name.title()}: {self.height}cm,\
 {self.age_days} days old")

    def grow(self, size: int) -> None:
        """
        Increase the plant's height by a given amount.

        Parameters
        ----------
        size : int
            The number of centimeters by which the plant should grow.
        """
        self.last_height = self.height
        self.height += size

    def age(self, days: int) -> None:
        """
        Increase the plant's age by a given number of days.

        Parameters
        ----------
        n : int
            The number of days to add to the plant's age.
        """
        self.last_age_days = self.age_days
        self.age_days += days

    def get_info(self) -> None:
        """
        Display detailed information about a plant, including its growth
        this week.

        Parameters
        ----------
        plant : Plant
            The Plant object whose information is to be displayed.
        """
        print(f"Growth this week: +{self.height - self.last_height}cm")


class PlantFactory:
    """
    A class to represent q factory for create plant.
    """
    factoryPlant: int = 0

    def create_plant(val: tuple[str, int, int]) -> Plant:
        """
        Create lot of plants

        Args:
            val tuple[str, int, int]: Table of values
        """
        PlantFactory.factoryPlant += 1
        name: str = ""
        height: int = 0
        age: int = 0
        name, height, age = val
        return Plant(name, height, age)


if __name__ == "__main__":
    plants_tuple = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)
        ]
    print("=== Plant Factory Output ===")

    plants = []
    for plant in plants_tuple:
        plants.append(PlantFactory.create_plant(plant))
    print()
    print(f"Total plants created: {PlantFactory.factoryPlant}")
