import os

def get_num_conflicts(file):
    fabric_matrix = [[0 for col in range(1000)] for row in range(1000)]

    with open(file, 'r') as f:
        lines = f.read().strip().splitlines()

    for claim in lines:
        claim = claim.split('@ ')[1].split(': ')
        
        x_pos, y_pos = claim[0].split(',')
        width, height = claim[1].split('x')

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(dir_path, 'day3.txt')

num_conflicts = get_num_conflicts(input_file)
print(checksum)
