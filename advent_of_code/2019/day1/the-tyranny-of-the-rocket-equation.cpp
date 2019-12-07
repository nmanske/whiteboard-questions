#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

int getFuelMass(int totalMass) {
  return totalMass / 3 - 2;
}

int main() {
  std::ifstream file("day1.txt");

  if (file.is_open()) {
    std::string line;
    int totalFuel = 0;
    int totalAdditionalFuel = 0;

    while(getline(file, line)) {
      int totalMass = std::stoi(line);

      // Part 1
      int fuelMass = getFuelMass(totalMass);
      totalFuel += fuelMass;

      // Part 2
      do {
        totalAdditionalFuel += fuelMass;
      } while ( (fuelMass = getFuelMass(fuelMass)) > 0);
    }

    file.close();

    std::cout << "Part 1: " << totalFuel << std::endl;
    std::cout << "Part 2: " << totalAdditionalFuel << std::endl;
  }
}
