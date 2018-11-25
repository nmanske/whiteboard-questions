'''Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Questions to ask: Are we assuming ASCII strings? Extended ASCII? Unicode?
'''

import unittest

# Runtime: O(n)
def isUniqueDict(s):
    # Assuming char set is standard ASCII
    if len(s) > 128:
        return False

    chars = {}
    for c in s:
        if c not in chars:
            chars[c] = 1
        else:
            return False

    return True

# Runtime: O(n log(n))
def isUniqueStr(s):
    # Assuming char set is standard ASCII
    if len(s) > 128:
        return False

    s = ''.join(sorted(s))
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            return False

    return True

class Test(unittest.TestCase):
    dataT = [('abcdefg'), ('8fna0('), ('')]
    dataF = [('2fjzn2'), ('hfa 843 ( (')]

    def test_unique_hash(self):
        for test_string in self.dataT:
            result = isUniqueDict(test_string)
            self.assertTrue(result)
        for test_string in self.dataF:
            result = isUniqueDict(test_string)
            self.assertFalse(result)

    def test_unique_str(self):
        for test_string in self.dataT:
            result = isUniqueStr(test_string)
            self.assertTrue(result)
        for test_string in self.dataF:
            result = isUniqueStr(test_string)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
