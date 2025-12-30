#!/usr/bin/env python3
"""Module to define the basic Plant class and show its info."""


class Plant:
    """Plant with basic attributes."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show_info(self):
        """Print the plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
rose.show_info()
sunflower.show_info()
cactus.show_info()
""" class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old") """
