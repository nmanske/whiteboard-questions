''' String - Problem 1
Find the first non-repeated character in a string
'''

import unittest

def check_unique(data):
    unique_char = None
    for i in data:
        count = 0
        for j in data:
            if i == j:
                count += 1
        if count == 1:
            unique_char = i
    return unique_char

class TestPairSum(unittest.TestCase):

    unique_data = "qwertyuiopasdfghjklzxcvbnmqwertyuioasdfghjklzxcvbnm"

    def test_unique(self):
        # pair sum check
        result = check_unique(self.unique_data)
        self.assertEqual(result, 'p')

if __name__ == "__main__":
    unittest.main()

