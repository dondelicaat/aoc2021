import os
from typing import List


class Bingo:
    def __init__(self, board: List[List]):
        self.board = board

    def bingo(self, number) -> bool:
        x, y = self.mark(number)

        # Not found on the board.
        if x == -1 and y == -1:
            return False

        column = True
        row = True
        # check column
        for i in range(5):
            if self.board[x][i] != -1:
                column = False

        # check row
        for i in range(5):
            if self.board[i][y] != -1:
                row = False

        return row or column

    def mark(self, number):
        for idx in range(5):
            for idy in range(5):
                if self.board[idx][idy] == number:
                    self.board[idx][idy] = -1
                    return idx, idy

        return -1, -1

    def get_score(self, number):
        sum = 0
        for idx in range(5):
            for idy in range(5):
                if self.board[idx][idy] != -1:
                    sum += self.board[idx][idy]

        return number * sum


def play(numbers, boards):
    bingo_boards = []
    for board in boards:
        bingo_boards.append(Bingo(board))

    for number in numbers:
        for idx, bingo_board in enumerate(bingo_boards):
            if bingo_board.bingo(number):
                score = bingo_board.get_score(number)
                print(f"Board {idx} won with score {score}")
                return

def play_to_lose(numbers, boards):
    bingo_boards = []
    for board in boards:
        bingo_boards.append(Bingo(board))

    last_winner = 0
    last_score = 0
    winners_list = []

    for number in numbers:
        for idx, bingo_board in enumerate(bingo_boards):
            if bingo_board.bingo(number) and idx not in winners_list:
                score = bingo_board.get_score(number)
                print(f"Board {idx} won with score {score}")
                winners_list.append(idx)
                last_winner = idx
                last_score = score

    print("last winner: ", last_winner)
    print("score:", last_score)


def parse_input():
    with open(f"{os.getcwd()}/day4/input.txt", "r") as f:
        lines = f.readlines()
        numbers = list(map(int, lines[0].strip().split(',')))

        boards = []
        idx = 2
        while idx < len(lines):
            board = []
            for i in range(5):
                row = list(map(int, lines[idx + i].strip().split()))
                board.append(row)

            boards.append(board)

            idx += 6
        return numbers, boards


def main():
    numbers, boards = parse_input()
    # play(numbers, boards)
    play_to_lose(numbers, boards)

main()
