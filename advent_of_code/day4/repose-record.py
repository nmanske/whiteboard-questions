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

def get_sleep_data(logs):
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

    return sleep_data

def highest_mins_asleep_info(sleep_data):
    highest_total_mins_asleep_guard = None
    highest_total_mins_asleep = 0
    most_frequent_minute = None

    for k1, v1 in sleep_data.items():
        total_mins_asleep = 0
        for k2, v2 in v1.items():
            total_mins_asleep += v2
        if (total_mins_asleep > highest_total_mins_asleep):
            highest_total_mins_asleep_guard = k1
            highest_total_mins_asleep = total_mins_asleep
            most_frequent_minute = 0
            for k2, v2 in v1.items():
                if v2 > most_frequent_minute:
                    most_frequent_minute = k2

    return highest_total_mins_asleep_guard, most_frequent_minute

def most_frequent_minute_asleep_info(sleep_data):
    most_frequent_minute_asleep_guard = None
    most_frequent_minute = None
    most_frequent_minute_value = 0

    for k1, v1 in sleep_data.items():
        for k2, v2 in v1.items():
            if v2 > most_frequent_minute_value:
                most_frequent_minute_asleep_guard = k1
                most_frequent_minute = k2
                most_frequent_minute_value = v2

    return most_frequent_minute_asleep_guard, most_frequent_minute

dir_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(os.path.join(dir_path, 'day4.txt'))
output_file = os.path.join(os.path.join(dir_path, 'day4_sorted.txt'))

sorted_logs = get_sorted_logs(input_file, output_file)
sleep_data = get_sleep_data(sorted_logs)

# Part 1
highest_total_mins_asleep_guard, most_frequent_minute = highest_mins_asleep_info(sleep_data)

print('Guard with highest total minutes asleep: ' + str(highest_total_mins_asleep_guard))
print('Most frequent minute: ' + str(most_frequent_minute) + '\n')

# Part 2
most_frequent_minute_asleep_guard, most_frequent_minute = most_frequent_minute_asleep_info(sleep_data)

print('Guard with most frequent sleep on minute: ' + str(most_frequent_minute_asleep_guard))
print('Most frequent minute: ' + str(most_frequent_minute))
