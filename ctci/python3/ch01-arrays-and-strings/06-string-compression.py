'''Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string. You can assume the string
has only uppercase and lowercase letters (a - z).'''

import unittest

def string_compression(s):
    result = ''
    count = 0

    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            result += s[i] + str(count)
            count = 0

    return result if len(result) < len(s) else s

# def string_compression_naive(s):
#     last = None
#     result = ''
#     count = 0

#     for c in s:
#         if last and c != last:
#             result += last + str(count)
#             count = 0
#         count += 1
#         last = c

#     result += last + str(count)

#     return result if len(result) < len(s) else s

class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef'),
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
