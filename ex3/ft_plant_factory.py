class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def display_plant_created(plants):
    count = 0
    for plant in plants:
        count += 1
        print("Created: " + plant.name + " (", plant.height, " cm, ",
              plant.age, " days)", sep="")
    print("\nTotal plants created:", count)


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    plant_list = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    display_plant_created(plant_list)
