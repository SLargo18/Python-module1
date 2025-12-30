#!/usr/bin/env python3
"""Module to print a simple welcome message for the garden."""


def main():
    """Initialize variables and print garden welcome information."""
    name = "Rose"
    height_cm = 25
    age_days = 30

    print("=== Welcome to my garden ===")
    print("Plant:", name)
    print("Height:", height_cm, "cm")
    print("Age:", age_days, "days")
    print("\n=== End of program ===")


if __name__ == "__main__":
    main()
