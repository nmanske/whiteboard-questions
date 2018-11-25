'''Given two strings, sl and s2, write code to check if s2 is a rotation of s1
using only one substring call (e.g., "waterbottle" is a rotation of
"erbottlewat").'''

import unittest

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return s2 in s1 * 2

class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
