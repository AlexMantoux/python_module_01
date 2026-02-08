class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, n):
        self.height += n

    def increase_age(self, n):
        self.age += n


def get_info(plant):
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
