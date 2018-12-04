import os

def get_num_conflicts(file):
    fabric = [[0 for col in range(1000)] for row in range(1000)]

    print(fabric[:][2])

    with open(file, 'r') as f:
        lines = f.read().strip().splitlines()

    for claim in lines:
        claim = claim.split('@ ')[1].split(': ')
        x_pos, y_pos = [int(c) for c in claim[0].split(',')]
        width, height = [int(c) for c in claim[1].split('x')]
        for i in range(x_pos, x_pos+width):
            for j in range(y_pos, y_pos+height):
                fabric[j][i] += 1

    num_conflicts = 0
    for i in range(1000):
        for j in range(1000):
            if fabric[j][i] >= 2:
                num_conflicts += 1

    return num_conflicts

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(dir_path, 'day3.txt')

num_conflicts = get_num_conflicts(input_file)
print(num_conflicts)
