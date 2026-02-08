class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def display_plant(plant):
    print(plant.name + ": ",
          plant.height, "cm, ", plant.age, " days old", sep="")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    display_plant(Plant("Rose", 25, 30))
    display_plant(Plant("SunFlower", 80, 45))
    display_plant(Plant("Cactus", 15, 120))
