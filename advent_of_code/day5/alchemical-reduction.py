import os

def get_reduction(file):
    with open(file, 'r') as f:
        formula = f.readline().strip()

    is_reaction = True
    while(is_reaction):
        is_reaction = False
        for i in range(0, len(formula)-1):
            if ((formula[i].isupper() and formula[i+1].islower()) or \
                (formula[i].islower() and formula[i+1].isupper())) and \
                formula[i].upper() == formula[i+1].upper():
                formula = formula[:i] + formula[i+2:]
                is_reaction = True
                break

    return formula

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(dir_path, 'day5.txt')

# Part 1

reduction = get_reduction(input_file)
print(reduction)
