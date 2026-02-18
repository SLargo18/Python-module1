#!/usr/bin/env python3
"""Module to manage a garden with different types of plants"""


class Plant:
    """Represents a basic plant with a name and height"""
    def __init__(self, name: str, height: int) -> None:
        """Represents a basic plant instance"""
        self.name: str = name
        self.height: int = height
        self.initial_h: int = height

    def get_info(self) -> str:
        """Return a string with the plant's name and current height"""
        return f"{self.name}: {self.height}cm"

    def get_type(self) -> str:
        """Return the category of the plant"""
        return "regular"

    def get_points(self) -> int:
        """Calculate the points based on the plant's height"""
        return self.height


class FloweringPlant(Plant):
    """Represents a plant that produces flowers of a specific color"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant with an additional color attribute"""
        super().__init__(name, height)
        self.color: str = color

    def get_info(self) -> str:
        """Return detailed info including the flower color"""
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)")

    def get_type(self) -> str:
        """Return the flowering category"""
        return "flowering"


class PrizeFlower(FloweringPlant):
    """Represents a high-quality flower that awards extra points"""
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        points: int
    ) -> None:
        """Initialize a prize flower with specific award points"""
        super().__init__(name, height, color)
        self.points = points

    def get_info(self) -> str:
        """Return full details including prize points"""
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming), "
                f"Prize points: {self.points}")

    def get_type(self) -> str:
        """Return the prize category"""
        return "prize"

    def get_points(self) -> int:
        """Return the specific points assigned to this prize flower"""
        return self.points


class GardenManager:
    """Manages a collection of plants and tracks multiple gardens"""
    gardens = []

    def __init__(self, owner: str) -> None:
        """Inizialize the manager with an owner and an empty plant list"""
        self.owner: str = owner
        self.plants: list = []
        GardenManager.gardens: list = GardenManager.gardens + [self]

    def add_plant(self, plant: Plant, show: bool = False) -> None:
        """Add a single plant to the garden and notify the user"""
        self.plants = self.plants + [plant]
        if not show:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def add_plants(self, *args) -> None:
        """Add multiple plant objects to the garden at once"""
        for i in args:
            self.add_plant(i)

    def grow_all(self):
        """Increase the height of all plants in the garden by 1cm"""
        for i in self.plants:
            i.height += 1
            print(f"{i.name} grew 1cm")

    class GardenStats:
        """Inner class to handle reporting and statistics of a garden"""
        @staticmethod
        def report(manager) -> None:
            """Print a complete status report of the given garden manager"""
            print(f"=== {manager.owner}'s Garden Report ===")
            print("Plants in garden:")

            total_plants = 0
            total_growth = 0
            regular = 0
            flowering = 0
            prize = 0
            total_points = 0

            for plant in manager.plants:
                print(f"- {plant.get_info()}")

                total_plants += 1
                total_growth += plant.height - plant.initial_h
                total_points += plant.get_points()

                if plant.get_type() == "regular":
                    regular += 1
                elif plant.get_type() == "flowering":
                    flowering += 1
                else:
                    prize += 1

            print(f"\nPlants added: {total_plants}, "
                  f"total growth: {total_growth}cm")

            print(f"Plant types: {regular} regular, "
                  f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls, names: list) -> list:
        """Create a multiple GardenManager instrances form a list of names"""
        return [cls(name) for name in names]

    @staticmethod
    def validate_height(height: int) -> bool:
        """Check if a given height value is valid"""
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    names = ["Alice", "Bob"]
    gardens = GardenManager.create_garden_network(names)

    alice_garden = gardens[0]
    bob_garden = gardens[1]

    data_list = [
        {"name": "Oak Tree", "height": 100},
        {"name": "Rose", "height": 25, "color": "red"},
        {"name": "Sunflower", "height": 50, "color": "yellow", "points": 10}
    ]

    plant_objects = []
    for data in data_list:
        if "points" in data:
            plant_objects += [PrizeFlower(**data)]
        elif "color" in data:
            plant_objects += [FloweringPlant(**data)]
        else:
            plant_objects += [Plant(**data)]

    alice_garden.add_plants(*plant_objects)
    bob_garden.add_plant(Plant("Old Bush", 92), show=True)

    print()
    print(f"{alice_garden.owner} is helping all plants grow...")
    alice_garden.grow_all()
    print()

    GardenManager.GardenStats.report(alice_garden)
    print()

    print(f"Height validation test: {GardenManager.validate_height(10)}")
    scores_str = ""
    for g in GardenManager.gardens:
        total_score = 0
        for p in g.plants:
            if p.get_type() == "prize":
                total_score += p.height + p.points
            else:
                total_score += p.height

        if g.owner == "Alice":
            total_score += 30

        if scores_str != "":
            scores_str += ", "
        scores_str += f"{g.owner}: {total_score}"

    print(f"Garden scores - {scores_str}")

    total_gardens = 0
    for g in GardenManager.gardens:
        total_gardens += 1
    print(f"Total gardens managed: {total_gardens}")
