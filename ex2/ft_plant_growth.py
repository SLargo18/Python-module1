class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def show_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self, height):
        self.height += height

    def age(self, days):
        self.days += days


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

plants = [rose, sunflower, cactus]
growth_amounts = [6, 3, 0.5]
actual_heights = [rose.height, sunflower.height, cactus.height]
i = 0
print("=== Day 1 ===")
for plant in plants:
    plant.show_info()

for plant in plants:
    plant.grow(growth_amounts[i])
    plant.age(6)
    i += 1

print("\n=== Day 7 ===")
j = 0
for plant in plants:
    growth = plant.height - actual_heights[j]
    plant.show_info()
    print(f"Growth this week: +{growth}cm")
    j += 1
