'''There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write 
a function to check if they are one edit (or zero edits) away.'''

import unittest

def is_one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    letters = {}
    for c in s1:
        letters[c] = letters.get(c, 0) + 1

    for c in s2:
        if letters.get(c, 0):
            letters[c] -= 1
    
    difference = sum(v for v in letters.values())

    if difference == 0 or difference == 1:
        return True

    return False

class Test(unittest.TestCase):
    data = (
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    )

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = is_one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
