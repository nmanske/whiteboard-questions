''' General - Problem 2
Find pairs in an integer array whose sum is equal to 10
'''

import unittest

def check_pair_sum(data):
    pairs = []
    for i in range(0, len(data)-1):
        if data[i] + data[i+1] == 10:
            pairs.append([data[i], data[i+1]])
    return pairs

class TestPairSum(unittest.TestCase):

    pair_sum_data = [3, 7, 1, -8, 10, 0, 2, -5, 4, 4, 6, 3, 12, -2]

    def test_pair_sum(self):
        # pair sum check
        result = check_pair_sum(self.pair_sum_data)
        expected = [[3, 7], [10, 0], [4, 6], [12, -2]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

