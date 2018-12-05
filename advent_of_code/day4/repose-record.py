import os
import re

from enum import Enum

class GuardAction(Enum):
    BEGIN = 1
    SLEEP = 2
    WAKE = 3

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
    sleep_data = {}
    current_guard = None
    sleep_start_minute = None
    for log in logs:
        log = log.strip().split(' ')

        date, time = log[0:2]
        year, month, day = list(map(int, date.split('-')))
        hour, minute = list(map(int, time.split(':')))

        action = None
        if 'Guard' in log:
            action = GuardAction.BEGIN
        elif 'asleep' in log:
            action = GuardAction.SLEEP
        elif 'wakes' in log:
            action = GuardAction.WAKE

        if action == GuardAction.BEGIN:
            current_guard = int(log[3].replace('#', ''))
        elif action == GuardAction.SLEEP:
            sleep_start_minute = minute
            if current_guard not in sleep_data:
                sleep_data[current_guard] = {}
        elif action == GuardAction.WAKE:
            for m in range(sleep_start_minute, minute):
                sleep_data[current_guard][m] = sleep_data[current_guard].get(m, 0) + 1

    laziest_guard = None
    most_mins_asleep = 0
    for k1, v1 in sleep_data.items():
        total_mins_asleep = 0
        for k2, v2 in v1.items():
            total_mins_asleep += v2
        if (total_mins_asleep > most_mins_asleep):
            laziest_guard = k1
            most_mins_asleep = total_mins_asleep
            most_slept_minute = 0
            for k2, v2 in v1.items():
                if v2 > most_slept_minute:
                    most_slept_minute = k2

    print(sleep_data)

    return laziest_guard, most_mins_asleep, most_slept_minute

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(os.path.join(dir_path, 'day4.txt'))
output_file = os.path.join(os.path.join(dir_path, 'day4_sorted.txt'))

sorted_logs = get_sorted_logs(input_file, output_file)
laziest_guard, most_mins_asleep, most_slept_minute = get_lazy_guard_info(sorted_logs)

print(str(laziest_guard) + ' / ' + str(most_mins_asleep) + ' / ' + str(most_slept_minute))
