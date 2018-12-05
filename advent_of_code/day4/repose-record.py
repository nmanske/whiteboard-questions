import os
import re

from enum import Enum

class GuardAction(Enum):
    BEGIN = auto()
    SLEEP = auto()
    WAKE = auto()

def get_sorted_logs(input_file, output_file):
    with open(input_file, 'r+') as f:
        lines = f.readlines()
        lines.sort()

    sorted_logs = []
    with open(output_file, 'w') as f:
        for line in lines:
            line = re.sub(r'([\[\]])', '', line)
            sorted_logs.append(line)
            f.write(line)

    return sorted_logs

def get_lazy_guard_info(logs):
    current_guard = None
    for log in logs:
        log = log.strip().split(' ')

        date, time = log[0:2]
        year, month, day = list(map(int, date.split('-')))
        hour, minute = list(map(int, time.split(':')))

        action = None
        if 'Guard' in log:
            current_guard = int(log[3].replace('#', ''))
            action = GuardAction.BEGIN
        elif 'asleep' in log:
            action = GuardAction.SLEEP
        elif 'wakes' in log:
            action = GuardAction.WAKE

    return None

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(os.path.join(dir_path, 'day4.txt'))
output_file = os.path.join(os.path.join(dir_path, 'day4_sorted.txt'))

sorted_logs = get_sorted_logs(input_file, output_file)
guard_id, most_slept_minute = get_lazy_guard_info(sorted_logs)
