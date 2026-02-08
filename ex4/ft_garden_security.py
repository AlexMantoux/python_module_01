class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the plant with name, age, and height.

        Args:
            name (str): The name of the plant.
            age (int): The age of the plant in days.
            height (int): The height of the plant in cm.
        """
        self.name: str = name
        self.__height: int = height
        self.__age_days: int = age
        print(f"Plant created: {self.name}")

    def display(self) -> None:
        """
        Display the plant's details.
        """
        print(f"Current plant: {self.name} ({self.get_height()}cm, \
{self.get_age()} days)")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age_days

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print()
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age_days = age
            print(f"Age updated: {age} days [OK]")
        else:
            print()
            print("Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 6, 30)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.display()
