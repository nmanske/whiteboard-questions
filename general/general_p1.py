''' General - Problem 1
Find the most frequent integer in an array
'''

import unittest

def check_mode(data):
    max_count = 0
    for i in data:
        count = 0
        for j in data:
            if i == j:
                count += 1
            if count > max_count:
                max_count = count
                max_value = i
    return max_value

class TestMode(unittest.TestCase):

    mode_data = [8, 10, 1, 4, 3, 7, 4]

    def test_mode(self):
        # mode check
        result = check_mode(self.mode_data)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()

