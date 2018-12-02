import os

def sum_frequency_changes(file):
    sum = 0
    with open (file, 'r') as f:
        for line in f:
            sum += int(line)
    return sum

dir_path = os.path.dirname(os.path.abspath(__file__))
print(sum_frequency_changes(os.path.join(dir_path, 'day1.txt')))
