# -*- coding: utf-8 -*-

'''Given a string, write a function to check if it is a permutation of a
palin­drome. A palindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters. The palindrome does not
need to be limited to just dictionary words.'''

import unittest

def is_palindrome_permutation(string):
    string = string.replace(' ', '').lower()
    letters = {}

    for c in string:
        letters[c] = letters.get(c, 0) + 1

    found_odd = False
    for v in letters.values():
        if v % 2 == 1:
            if found_odd == True:
                return False
            found_odd = True

    return True


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True),
    ]

    def test_palindrome_permutation(self):
        for [test_string, expected] in self.data:
            actual = is_palindrome_permutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
