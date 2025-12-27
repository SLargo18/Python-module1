class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


each_plant = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
]

i = 0
print("=== Plant Factory Output ===")
for name, height, age in each_plant:
    plant_created = Plant(name, height, age)
    print(f"Created: {plant_created.name} "
          f"({plant_created.height}cm, {plant_created.age} days)")
    i += 1
print(f"\nTotal plants created: {i}")
