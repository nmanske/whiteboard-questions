#include <iostream>
#include <vector>

void printVector(const std::vector<int>& vec) {
  for (const auto& i : vec)
    std::cout << i << ' ';

  std::cout << std::endl;
}

void selectionSort(std::vector<int>& vec) {
  const int N = vec.size();


}

int main() {
  std::vector<int> vec {4, 5, 10, 7, 3, 1, 6, 2, 9, 8};

  std::cout << "Before sorting: ";
  printVector(vec);

  selectionSort(vec);

  std::cout << "After sorting: ";
  printVector(vec);
}
