import os
import csv

def corruption_checksum_subtraction(sheet):
    checksum = 0
    for row in sheet:
        row = sorted(row)
        min_val = row[0]
        max_val = row[-1]
        checksum += max_val - min_val
    return checksum

def get_even_division_result(row):
    for i in range(len(row)):
        for j in range(i+1, len(row)):
            if row[i] % row[j] == 0:
                return row[i] // row[j]
    return None

def corruption_checksum_division(sheet):
    checksum = 0
    for row in sheet:
        row = sorted(row, reverse=True)
        result = get_even_division_result(row)
        checksum += result
    return checksum

dir_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir_path, 'day2.txt')

sheet = []
with open(file, 'r') as f:
    tsvin = csv.reader(f, delimiter='\t')
    for row in tsvin:
        sheet.append(list(map(int, row)))

# Part 1
checksum_subtraction = corruption_checksum_subtraction(sheet)
print(checksum_subtraction)

# Part 2
checksum_division = corruption_checksum_division(sheet)
print(checksum_division)
