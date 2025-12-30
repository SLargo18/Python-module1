#!/usr/bin/env python3
"""Module to simulate plant grwoth and aging over time."""


class Plant:
    """Plant class that can grow and age."""
    def __init__(self, name: str, height: float, days: int) -> None:
        """Initialize attributes"""
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def get_info(self) -> None:
        """Display current state of the plant"""
        print(f"{self.name}: {int(self.height)}cm, {self.days} days old")

    def grow(self, height: float) -> None:
        """Add cenitmeters to the current height"""
        self.height += height

    def age(self, days: int) -> None:
        """Add days to the current age"""
        self.days += days


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]
    growth_amounts = [6, 3, 0.5]
    actual_heights = [rose.height, sunflower.height, cactus.height]

    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()

    i = 0
    for plant in plants:
        plant.grow(growth_amounts[i])
        plant.age(6)
        i += 1

    print("\n=== Day 7 ===")
    j = 0
    for plant in plants:
        growth_diff = plant.height - actual_heights[j]
        plant.get_info()
        print(f"Growth this week: +{int(growth_diff)}cm")
        j += 1
