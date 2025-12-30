#!/usr/bin/env python3
"""Module to create multiple plant objects"""


class Plant:
    """Plant whit basic atributtes"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initilize the plant instance with its starting values"""
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == "__main__":
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    i = 0
    print("=== Plant Factory Output ===")
    for name, height, age in plant_data:
        plant_created = Plant(name, height, age)
        print(f"Created: {plant_created.name} "
              f"({plant_created.height}cm, {plant_created.age} days)")
        i += 1

    print(f"\nTotal plants created: {i}")
