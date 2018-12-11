import os
import re

UPPERCASE_A = 65 # ASCII decimal
NUM_LETTERS = 26

def get_reduction(polymer):
    is_reaction = True
    while(is_reaction):
        is_reaction = False
        for i in range(0, len(polymer)-1):
            if ((polymer[i].isupper() and polymer[i+1].islower()) or \
                (polymer[i].islower() and polymer[i+1].isupper())) and \
                polymer[i].upper() == polymer[i+1].upper():
                polymer = polymer[:i] + polymer[i+2:]
                is_reaction = True
                break

    return polymer

def get_improved_reduction(polymer):
    shortest_polymer = None

    for i in range(NUM_LETTERS):
        letter_code = hex(UPPERCASE_A + i).replace('0x', '')
        pattern = r'([\x' + letter_code + r'])+'
        modified_polymer = re.sub(pattern, '', polymer, flags=re.IGNORECASE)
        reduced_modified_polymer = get_reduction(modified_polymer)
        if shortest_polymer is None or len(reduced_modified_polymer) < len(shortest_polymer):
            shortest_polymer = reduced_modified_polymer

    return shortest_polymer

dir_path = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(dir_path, 'day5.txt')
with open(input_file, 'r') as f:
    polymer = f.readline().strip()

# Part 1

reduction = get_reduction(polymer)
print('Reduction length: ' + str(len(reduction)))

reduction_file = os.path.join(os.path.join(dir_path, 'day5_reduction.txt'))
with open(reduction_file, 'w') as f:
    f.write(reduction)

# Part 2

improved_reduction = get_improved_reduction(polymer)
print('Improved reduction length: ' + str(len(improved_reduction)))

improved_reduction_file = os.path.join(os.path.join(dir_path, 'day5_improved_reduction.txt'))
with open(improved_reduction_file, 'w') as f:
    f.write(improved_reduction)
