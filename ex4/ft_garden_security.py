class Plant:
    def __init__(self, name, height, age):
        self.name = name
        print("Plant created: " + self.name)
        self._height = self.set_height(height)
        self._age = self.set_age(age)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height >= 0:
            self._height = height
            print("Height updated: ", height, " cm [OK]", sep="")
        else:
            print("\nInvalid operation attempted: height ", height,
                  " cm [REJECTED]", sep="")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self._height = age
            print("Age updated: ", age, " days [OK]", sep="")
        else:
            print("\nInvalid operation attempted: age ", age,
                  " days [REJECTED]", sep="")
            print("Security: Negative age rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 6, 30)
    rose.set_height(-5)
