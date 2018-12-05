import os
import re

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
        minute = int(log[1].split(':')[1])

        if 'Guard' in log:
            current_guard = int(log[3].replace('#', ''))
        elif 'asleep' in log:
            sleep_start_minute = minute
            if current_guard not in sleep_data:
                sleep_data[current_guard] = {}
        elif 'wakes' in log:
            for m in range(sleep_start_minute, minute):
                sleep_data[current_guard][m] = sleep_data[current_guard].get(m, 0) + 1

    laziest_guard = None
    laziest_minute = None
    laziest_total_mins_asleep = 0

    for k1, v1 in sleep_data.items():
        total_mins_asleep = 0
        for k2, v2 in v1.items():
            total_mins_asleep += v2
        if (total_mins_asleep > laziest_total_mins_asleep):
            laziest_guard = k1
            laziest_total_mins_asleep = total_mins_asleep
            laziest_minute = 0
            for k2, v2 in v1.items():
                if v2 > laziest_minute:
                    laziest_minute = k2

    return laziest_guard, laziest_minute

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(os.path.join(dir_path, 'day4.txt'))
output_file = os.path.join(os.path.join(dir_path, 'day4_sorted.txt'))

sorted_logs = get_sorted_logs(input_file, output_file)
laziest_guard, laziest_minute = get_lazy_guard_info(sorted_logs)

print('Laziest guard: ' + str(laziest_guard))
print('Laziest minute: ' + str(laziest_minute))
