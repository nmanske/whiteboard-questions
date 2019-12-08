#include <stdio.h>

int binary_search(int arr[], int low, int high, int x) {
  int mid;

  if (high >= low) {
    mid = low + (high - low) / 2;
    if (arr[mid] == x) return mid;
    if (arr[mid] > x) return binary_search(arr, low, mid - 1, x);
    else return binary_search(arr, mid + 1, high, x);
  }

  return -1;
}

int main(void) {
  int arr[] = { 2, 3, 4, 10, 40 };
  int n = sizeof(arr) / sizeof(arr[0]);
  int x = 10;

  int result = binary_search(arr, 0, n-1, x);

  (result == -1) ? puts("Element not present in array")
                 : printf("Element found at index %d", result);

  return 0;
}
