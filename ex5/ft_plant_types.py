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

    def display(self) -> None:
        """
        Display the plant's details.
        """
        print(f"{self.height}cm, {self.age_days} days old", end="")


class Flower(Plant):
    """
    Represents a flower with a name, height, age and color. 

    Attributes
    ----------
    name : str
        The name of the Flower.
    height : int
        The height of the Flower in centimeters.
    age : int
        The age of the Flower in days.
    color : str
        The color of the Flower.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize the Flower with name, height, age and color.

        Args:
            name (str): The name of the Flower.
            height (int): The height of the Flower in cm.
            age (int): The age of the Flower in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def display(self) -> None:
        """
        Display the plant's details.
        """
        print(f"{self.name} (Flower): ", end="")
        super().display()
        print(f", {self.color} color")

    def bloom(self) -> None:
        """
        simulate and display flower blooming
        """
        print(f"{self.name} is blooming beautifully!")
    
class Tree(Plant):
    """
    Represents a tree with a name, height, age and trunk_diameter. 

    Attributes
    ----------
    name : str
        The name of the tree.
    height : int
        The height of the tree in centimeters.
    age : int
        The age of the tree in days.
    trunk_diameter : int
        The trunk diameter of the tree.
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        """
        Initialize the tree with name, height, age and trunk diameter.

        Args:
            name (str): The name of the tree.
            height (int): The height of the tree in cm.
            age (int): The age of the tree in days.
            trunk_diameter (int): The trunk diameter of the tree.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def display(self) -> None:
        """
        Display the plant's details.
        """
        print(f"{self.name} (Tree): ", end="")
        super().display()
        print(f", {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """
        Compute and display the shade provide by the tree
        """
        print(f"{self.name} provides {78} square meters of shade")

class Vegetable(Plant):
    """
    Represents a vegetable with a name, height, age, harvest season and nutritional value. 

    Attributes
    ----------
    name : str
        The name of the vegetable.
    height : int
        The height of the vegetable in centimeters.
    age : int
        The age of the vegetable in days.
    harvest_season : str
        The harvest season of the vegetable.
    nutritional_value : str
        The nutritional value of the vegetable.
    """
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize the vegetable with name, height, age, harvest season and nutritional value.

        Args:
            name (str): The name of the vegetable.
            height (int): The height of the vegetable in cm.
            age (int): The age of the vegetable in days.
            harvest_season (str): The harvest season of the vegetable.
            nutritional_value (str): The nutritional value of the vegetable.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display(self) -> None:
        """
        Display the plant's details.
        """
        print(f"{self.name} (Vegetable): ", end="")
        super().display()
        print(f", {self.harvest_season} harvest")
    
    def get_nutri_info(self) -> None:
        """
        Display nutritional value
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1850, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print("=== Garden Plant Types ===")
    print()

    rose.display()
    rose.bloom()
    print()

    oak.display()
    oak.produce_shade()
    print()

    tomato.display()
    tomato.get_nutri_info()
