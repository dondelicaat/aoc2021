import os


def get_input():
    with open(f"{os.getcwd()}/day1/input.txt", "r") as f:
        measurements = [int(measurement_txt) for measurement_txt in f.readlines()]
    return measurements


def get_windowed_measurements(input, window_size):
    print(len(input))
    windowed_input = list()
    for idx, value in enumerate(input):
        if len(input) <= (idx + window_size - 1):
            break
        windowed_input.append(sum(input[idx:idx + window_size]))

    return windowed_input


def count_increasing(input):
    num_increasing = 0
    for idx, current_value in enumerate(input):
        if idx == 0:
            continue
        if current_value > input[idx - 1]:
            num_increasing += 1
    return num_increasing


def run():
    input = get_input()
    measurements = get_windowed_measurements(input, 3)
    num_increasing = count_increasing(measurements)
    print("num increasing", num_increasing)



run()
