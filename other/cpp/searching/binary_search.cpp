#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& vec, int low, int high, int x) {
  int mid = low + (high - low) / 2;

  if (high >= low) {
    if (vec[mid] == x) {
      return mid;
    } else if (vec[mid] > x) {
      return binarySearch(vec, low, mid - 1, x);
    } else {
      return binarySearch(vec, mid + 1, high, x);
    }
  }

  return -1;
}

int main() {
  std::vector<int> sorted_list {2, 3, 4, 10, 40};

  int result = binarySearch(sorted_list, 0, sorted_list.size() - 1, 10);

  if (result == -1) {
    std::cout << "Element not found in vector" << std::endl;
  } else {
    std::cout << "Element found at index " << result << std::endl;
  }
}
