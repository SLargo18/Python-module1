class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = 0
        self._age: int = 0

        print(f"Plant created: {self._name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self._height

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def get_age(self) -> int:
        return self._age

    def set_age(self, value1: int) -> None:
        if value1 < 0:
            print(f"\nInvalid operation attempted: "
                  f"age {value1} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value1
            print(f"Age updated: {value1} days [OK]")

    def __str__(self) -> str:
        return (f"\nCurrent plant: {self._name}"
                f"({self._height}cm, {self._age} days)")


""" if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-4)
    print(rose)
 """
