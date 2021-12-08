import os
import sys


def get_data():
    with open(f"{os.getcwd()}/day7/sampleinput.txt", "r") as f:
        return list(map(int, f.readline().split(',')))


def run():
    positions = get_data()
    min_pos = min(positions)
    max_pos = max(positions)

    min_cost = sys.maxsize
    optimal_position = -1
    for alignment_position in range(min_pos, max_pos + 1):
        cost = 0
        for position in positions:
            cost += sum(range(abs(position - alignment_position) + 1))
        if cost < min_cost:
            min_cost = cost
            optimal_position = alignment_position

    print(min_cost)
    print(optimal_position)

run()
