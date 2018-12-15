import os

def next_digit_matches(captcha):
    solution = 0

    for i in range(len(captcha)):
        digit_1 = int(captcha[i])
        digit_2 = int(captcha[0]) if i == len(captcha) - 1 else int(captcha[i+1])
        if digit_1 == digit_2:
            solution += digit_1

    return solution

def halfway_around_matches(captcha):
    original_len = len(captcha)
    captcha = captcha * 2
    solution = 0

    for i in range(original_len):
        digit_1 = int(captcha[i])
        digit_2 = int(captcha[i+original_len//2])
        if digit_1 == digit_2:
            solution += digit_1

    return solution

dir_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir_path, 'day1.txt')

with open(file, 'r') as f:
    captcha = f.readline().strip()

next_solution = next_digit_matches(captcha)
print(next_solution)

halfway_solution = halfway_around_matches(captcha)
print(halfway_solution)
