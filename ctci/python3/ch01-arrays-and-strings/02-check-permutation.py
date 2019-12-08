'''Given two strings, write a method to decide if one is a permutation
of the other.

Questions to ask: Is the comparison case sensitive? What about whitespace?
'''

import unittest

def isPermutationSort(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_sorted = ''.join(sorted(s1))
    s2_sorted = ''.join(sorted(s2))

    return s1_sorted == s2_sorted

def isPermutationCounter(s1, s2):
    if len(s1) != len(s2):
        return False

    chars = {}

    for c in s1:
        chars[c] = chars.get(c, 0) + 1

    for c in s2:
        if chars.get(c, 0) == 0:
            return False
        chars[c] -= 1

    return True

class Test(unittest.TestCase):
    dataT = [
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    ]
    dataF = [
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    ]

    def test_permutation_sort(self):
        for test_strings in self.dataT:
            result = isPermutationSort(*test_strings)
            self.assertTrue(result)
        for test_strings in self.dataF:
            result = isPermutationSort(*test_strings)
            self.assertFalse(result)

    def test_permutation_counter(self):
        for test_strings in self.dataT:
            result = isPermutationCounter(*test_strings)
            self.assertTrue(result)
        for test_strings in self.dataF:
            result = isPermutationCounter(*test_strings)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
