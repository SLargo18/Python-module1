#!/usr/bin/env python3
"""Module to provide data security and encapsulation for garden plants"""


class SecurePlant:
    """Class representing a plant with data validation and protection."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = 0
        self._age: int = 0

        print(f"Plant created: {self._name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """Securley acces the plant's height"""
        return self._height

    def set_height(self, value: int) -> None:
        """Validate and set plant height"""
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def get_age(self) -> int:
        """securley access the plant's age"""
        return self._age

    def set_age(self, value: int) -> None:
        """Validate and set plant age"""
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-4)
    print(f"\nCurrent plant: {rose._name} "
          f"{rose.get_height()}cm, {rose.get_age()} dyas")
