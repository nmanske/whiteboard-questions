import os
import re

def get_sorted_logs(input_file, output_file):
    with open(input_file, 'r+') as f:
        lines = f.readlines()
        lines.sort().

    sorted_logs = []
    with open(output_file, 'w') as f:
        for line in lines:
            line = re.sub(r'([\[\]])', '', line)
            sorted_logs.append(line)
            f.write(line)

    return sorted_logs

def get_lazy_guard_info(logs):
    for log in logs:
        pass

    return None

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(os.path.join(dir_path, 'day4.txt'))
output_file = os.path.join(os.path.join(dir_path, 'day4_sorted.txt'))

sorted_logs = get_sorted_logs(input_file, output_file)
guard_id, most_slept_minute = get_lazy_guard_info(sorted_logs)
