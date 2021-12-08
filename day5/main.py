import os
from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
    start: Point
    end: Point


class Map:
    def __init__(self, x: int, y: int):
        self.x_max = x + 1
        self.y_max = y + 1
        self.map = []
        for x in range(self.x_max):
            self.map.append([])
            for y in range(self.y_max):
                self.map[x].append(0)

    def add_line(self, line):
        start = line.start
        end = line.end

        points = []

        if start.x == end.x:
            if start.y < end.y:
                y_coordinates = range(start.y, end.y + 1)
            else:
                y_coordinates = range(end.y, start.y + 1)

            for y in y_coordinates:
                points.append(Point(start.x, y))

        elif start.y == end.y:
            if start.x < end.x:
                x_coordinates = range(start.x, end.x + 1)
            else:
                x_coordinates = range(end.x, start.x + 1)

            for x in x_coordinates:
                points.append(Point(x, start.y))

        else:
            # only 45 degrees.
            if start.y < end.y:
                y_coordinates = list(range(start.y, end.y + 1))
                y_coordinates = sorted(y_coordinates, reverse=True)
            else:
                y_coordinates = list(range(end.y, start.y + 1))

            if start.x < end.x:
                x_coordinates = list(range(start.x, end.x + 1))
                x_coordinates = sorted(x_coordinates, reverse=True)
            else:
                x_coordinates = list(range(end.x, start.x + 1))

            for i in range(len(x_coordinates)):
                points.append(Point(x_coordinates[i], y_coordinates[i]))

        for point in points:
            self.add_point(point)

    def add_point(self, point: Point):
        self.map[point.x][point.y] += 1

    def print_map(self):
        map_string = ""
        for y in range(self.y_max):
            for x in range(self.x_max):
                if self.map[x][y] == 0:
                    map_string += "."
                else:
                    map_string += str(self.map[x][y])
            map_string += "\n"

        print(map_string)

    def get_num_overlapping(self):
        count = 0
        for y in range(self.y_max):
            for x in range(self.x_max):
                if self.map[x][y] > 1:
                    count += 1

        return count

def parse_input():
    x_max = 0
    y_max = 0
    line_elements = []

    with open(f"{os.getcwd()}/day5/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            points = line.strip().split(" -> ")
            x_start, y_start = map(int, points[0].split(','))
            x_end, y_end = map(int, points[1].split(','))
            start = Point(x_start, y_start)
            end = Point(x_end, y_end)

            line_elt = Line(start, end)
            line_elements.append(line_elt)

            x_max = max(x_max, x_start, x_end)
            y_max = max(y_max, y_start, y_end)

    return line_elements, x_max, y_max


def main():
    lines, x_max, y_max = parse_input()
    map = Map(x_max, y_max)
    for line in lines:
        map.add_line(line)

    map.print_map()
    print(map.get_num_overlapping())

main()
