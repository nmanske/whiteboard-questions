#include <iostream>
#include <vector>

// Dynamic programming
int dynamicFib(int n) {
  std::vector<int> f {0, 1};

  for (int i = 2; i <= n; i++) {
    f.push_back(f[i-1] + f[i-2]);
  }

  return f[n];
}

// Recursion
int recursiveFib(int n) {
  if (n <= 1) return n;
  return recursiveFib(n-1) + recursiveFib(n-2);
}

int main() {
  int n;

  n = dynamicFib(10);
  std::cout << n << std::endl;

  n = recursiveFib(10);
  std::cout << n << std::endl;
}
