import os

def get_total_fuel(file: str) -> None:
    with open(file) as f:
        total_fuel = 0
        for line in f:
            total_mass = int(line)
            fuel_mass = total_mass // 3 - 2
            total_fuel += fuel_mass
        return total_fuel

# Part 1
total_fuel = get_total_fuel("day1.txt")
print(total_fuel)
