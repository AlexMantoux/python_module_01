class SecurePlant:
    """
    Class that represent a plant with secure entry and variables
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
        self._height: int = height
        self._age: int = age
        print(f"Plant created: {self.name}")

    def display(self) -> None:
        """
        Display the plant's details.
        """
        print(f"Current plant: {self.name} ({self.get_height()}cm, "
              f"{self.get_age()} days)")

    def get_height(self) -> int:
        """
        Return the current height value in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """
        Return the current age value in days.
        """
        return self._age

    def set_height(self, height: int) -> None:
        """
        Set the height value if it is non-negative.

        Args:
            height (int): The new height in centimeters. Must be greater than
            or equal to 0.
        """
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        Set the age value if it is non-negative.

        Args:
            age (int): The new age in days. Must be greater than
            or equal to 0.
        """
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 1, 1)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.display()
