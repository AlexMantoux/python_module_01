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

    def display(self):
        """
        Display the plant's details.
        """
        print(f"{self.name.title()}: {self.height}cm,\
 {self.age_days} days old")


class Flower(Plant):


    
class Tree(Plant):
class Vegetables(Plant):
if __name__ == "__main__":
    print("=== Garden Plant Types ===")
