def sum_frequency_changes(file):
    sum = 0
    with open (file, 'r') as f:
        for line in f:
            sum += int(line)
    return sum

print(sum_frequency_changes('day1.txt'))
