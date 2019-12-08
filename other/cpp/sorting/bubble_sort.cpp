#include <iostream>
#include <vector>

void printVector(const std::vector<int>& vec) {
  for (const auto& i : vec)
    std::cout << i << ' ';

  std::cout << std::endl;
}

void bubbleSort(std::vector<int>& vec) {
  const int N = vec.size();

  for (int i = 0; i < N - 1; i++) {
    bool swapped = false;

    for (int j = 0; j < N - i - 1; j++) {
      if (vec[j] > vec[j+1]) {
        std::swap(vec[j], vec[j+1]);
        swapped = true;
      }
    }

    if (not swapped) break;
  }
}

int main() {
  std::vector<int> vec {4, 5, 10, 7, 3, 1, 6, 2, 9, 8};

  std::cout << "Before sorting: ";
  printVector(vec);

  bubbleSort(vec);

  std::cout << "After sorting: ";
  printVector(vec);
}
