import os
from collections import Counter

# Part 1

def calculate_checksum(file):
    c2 = 0
    c3 = 0

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            letter_counts = Counter(line).values()
            if 2 in letter_counts:
                c2 += 1
            if 3 in letter_counts:
                c3 += 1

    return c2 * c3

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(dir_path, 'day2.txt')

checksum = calculate_checksum(input_file)
print(checksum)

# Part 2

def common_letters_correct_ids(file):
    with open(file, 'r') as f:
        lines = f.read().strip().splitlines()

    for i in lines:
        for j in lines:
            diff_count = 0
            diff_index = None
            for k, (c1, c2) in enumerate(zip(i, j)):
                if c1 != c2:
                    diff_count += 1
                    diff_index = k
                if diff_count > 1:
                    break
            if diff_count == 1:
                return i[:diff_index] + i[diff_index+1:]

    return None

common_letters = common_letters_correct_ids(input_file)
print(common_letters)
