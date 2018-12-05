import os

def get_sorted_logs(file):
    with open(file, 'r+') as f:
        lines = f.readlines()
        return lines.sort()

def get_vulnerable_guard_info(logs):
    return None

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(os.path.join(dir_path, 'day4.txt'))

sorted_logs = get_sorted_logs(input_file)
guard_id, minutes_asleep = get_vulnerable_guard_info(sorted_logs)
