import os

FABRIC_WIDTH = 1000
FABRIC_HEIGHT = 1000

def get_fabric_state(file):
    fabric = [[[] for col in range(FABRIC_WIDTH)] for row in range(FABRIC_HEIGHT)]
    conflict_ids = []

    with open(file, 'r') as f:
        lines = f.read().strip().splitlines()

    for claim in lines:
        claim_id, location_info = claim.split('@ ')
        claim_id = claim_id[1:]
        location_info = location_info.split(': ')
        x_pos, y_pos = [int(c) for c in location_info[0].split(',')]
        width, height = [int(c) for c in location_info[1].split('x')]
        for i in range(x_pos, x_pos+width):
            for j in range(y_pos, y_pos+height):
                fabric[j][i].append(claim_id)
                if len(fabric[j][i]) > 1:
                    for entry in fabric[j][i]:
                        if entry not in conflict_ids:
                            conflict_ids.append(entry)

    return fabric, conflict_ids

def get_num_conflicts(fabric):
    num_conflicts = 0
    for i in range(FABRIC_WIDTH):
        for j in range(FABRIC_HEIGHT):
            if len(fabric[j][i]) > 1:
                num_conflicts += 1
    return num_conflicts

def get_no_conflict_id(fabric, conflict_ids):
    for i in range(FABRIC_WIDTH):
        for j in range(FABRIC_HEIGHT):
            if len(fabric[j][i]) == 1 and fabric[j][i][0] not in conflict_ids:
                return fabric[j][i][0]

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(dir_path, 'day3.txt')

fabric, conflict_ids = get_fabric_state(input_file)
num_conflicts = get_num_conflicts(fabric)
no_conflict_id = get_no_conflict_id(fabric, conflict_ids)
print(num_conflicts)
print(no_conflict_id)
