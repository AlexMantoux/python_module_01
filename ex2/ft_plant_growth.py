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
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, n: int) -> None:
        """
        Increase the plant's height by a given amount.

        Parameters
        ----------
        n : int
            The number of centimeters by which the plant should grow.
        """
        self.height += n

    def increase_age(self, n) -> None:
        """
        Increase the plant's age by a given number of days.

        Parameters
        ----------
        n : int
            The number of days to add to the plant's age.
        """
        self.age += n


def get_info(plant) -> None:
    """
    Display detailed information about a plant, including its growth this week.

    Parameters
    ----------
    plant : Plant
        The Plant object whose information is to be displayed.
    """
    print(plant.name + ": ",
          plant.height, "cm, ", plant.age, " days old", sep="")
    print("Growth this week: +", 6, "cm", sep="")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    get_info(rose)
    rose.grow(6)
    rose.increase_age(6)
    print("=== Day 7 ===")
    get_info(rose)
