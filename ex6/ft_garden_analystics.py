#!/usr/bin/env python3
"""Module to manage a garden"""


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def get_info(self) -> str:
         return f"{self.name}: {self.height}cm"

    def get_type(self) -> str:
         return "regular"

    def get_points(self) -> int:
         return 0

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color

    def get_info(self) -> str:
         return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
        def __init__(self, name: str, height: int, color: str, points: int) -> None:
            super().__init__(name, height, color)
            self.points = points
        def get_info(self) -> str:
            return f"{self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.points}"

class GardenManager: #crear un garden Manager
    """"""
    def __init__(self, owner: str) -> None:
         """Inizialize the manager with an owner and an empty plant list"""
         self.owner: str = owner
         self.plants: list = []

    def add_plant(self, plant: Plant) -> None:
         self.plants = self.plants + [plant]
         print(f"Added {plant.name} to {self.owner}'s garden")

    def add_plants(self, *args) -> None:
         for i in args:
                self.add_plant(i)

    def grow_all(self):
         for i in self.plants:
              i.height += 1
              print(f"{i.name} grew 1cm")

    class GardenStats:
        @staticmethod
        def report(manager) -> None:
            print(f"=== {manager.owner}'s Garden Report ===")
            print("Plants in garden:")
            count = 0
            for i in manager.plants:
                 count += 1
            print(f"Garden Owner: {manager.owner}")
            print(f"Total plants: {count}")

    @classmethod
    def create_garden_network(cls, names: list) -> list:
         """Create a list of GardenManager instrances form a list of names"""
         return [cls(name) for name in names]

    @staticmethod
    def validate_height(height: int) -> bool:
         """Utility function to check a valid height"""
         return height >= 0

if __name__ == "__main__":

    names = ["Alice", "Bob"]
    gardens = GardenManager.create_garden_network(names)
    alice_garden = gardens[0]
    bob_garden = gardens[1]

    data_list = [
        {"name": "Rose", "height": 20, "color": "Red"},
        {"name": "Tulip", "height": 15, "color": "Yellow"},
        {"name": "Sunflower", "height": 50, "color": "Yellow"}
    ]

    plant_objects = [FloweringPlant(**data) for data in data_list]
    alice_garden.add_plants(*plant_objects)
    print("-" * 20)
    GardenManager.GardenStats.report(alice_garden)
