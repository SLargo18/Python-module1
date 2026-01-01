#!/usr/bin/env python3
"""Module to manage different types of garden plants"""


class Plant:
    """Base class / father"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initilze basic plant attributes"""
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """Specialized plant that can bloom and has a specific color"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def get_info(self) -> None:
        """Print flower's specific information"""
        print(f"{self.name} (Flower): {self.height}cm,"
              f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        """action showing the flower is blooming"""
        print(f"{self.name} is blooming beautifully!")

    def perform_action(self) -> None:
        """Execute the flower's unique behavior"""
        self.bloom()


class Tree(Plant):
    """Specialized plant that provides shade based on its size"""
    def __init__(self, name: str, height: int,
                 age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = diameter

    def get_info(self) -> None:
        """Print tree's specific information"""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,"
              f"{self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Calculate and print the shade area in square meters"""
        crown_radius = (self.height / 100) * 0.5
        shade_area = 3.14 * (crown_radius ** 2)
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def perform_action(self) -> None:
        """Execute the tree's unique behavior"""
        self.produce_shade()


class Vegetable(Plant):
    """Specialized plant grown for food with nutriotional valu"""
    def __init__(self, name: str, height: int,
                 age: int, season: str, nutrition: str) -> None:
        """Initialize vegetable with parent traits and food info"""
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = nutrition

    def get_info(self) -> None:
        """Print vegetable's specific information"""
        print(f"{self.name} (Vegetable): {self.height}cm,"
              f"{self.age} days, {self.harvest_season} harvest")

    def display_nutrition(self) -> None:
        """Print the nutritional benefits of begetable"""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def perform_action(self) -> None:
        """Execute the tree's unique behavior"""
        self.display_nutrition()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    garden = [
        Flower("Rose", 80, 3, "red"),
        Flower("Tulip", 45, 2, "yellow"),
        Tree("Oak", 500, 1825, 20),
        Tree("Pine", 150, 300, 5),
        Vegetable("Tomato", 80, 60, "summer", "vitamin C"),
        Vegetable("Carrot", 25, 70, "winter", "vitamin A")
    ]

    for plant in garden:
        print()
        plant.get_info()
        plant.perform_action()
