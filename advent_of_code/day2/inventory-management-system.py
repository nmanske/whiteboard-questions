import os
from collections import Counter

# Part 1

def calculate_checksum(file):
    total = [0, 0]

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            letter_counts = Counter(line).values()
            if 2 in letter_counts:
                total[0] += 1
            if 3 in letter_counts:
                total[1] += 1

    checksum = total[0] * total[1]
    return checksum

dir_path = os.path.dirname(os.path.abspath(__file__))
checksum = calculate_checksum(os.path.join(dir_path, 'day2.txt'))
print(checksum)

# Part 2

