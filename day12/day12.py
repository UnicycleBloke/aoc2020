import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math


def part1(data):
    x = 0
    y = 0
    a = 90

    for d in data:
        if (d[0] == 'N'): y = y + d[1]
        if (d[0] == 'S'): y = y - d[1]
        if (d[0] == 'E'): x = x + d[1]
        if (d[0] == 'W'): x = x - d[1]
        if (d[0] == 'L'): a = a - d[1]
        if (d[0] == 'R'): a = a + d[1]
        if (d[0] == 'F'):
            x = x + math.sin(a * math.pi / 180) * d[1]
            y = y + math.cos(a * math.pi / 180) * d[1]

    return int(abs(x) + abs(y) + 0.001)  


def part2(data):
    x  = 10
    y  = 1
    sx = 0
    sy = 0 

    for d in data:
        if (d[0] == 'N'): y = y + d[1]
        if (d[0] == 'S'): y = y - d[1]
        if (d[0] == 'E'): x = x + d[1]
        if (d[0] == 'W'): x = x - d[1]
        if (d[0] == 'L'):
            a  = d[1] * math.pi / 180 
            x2 = x * math.cos(a) - y * math.sin(a)
            y2 = x * math.sin(a) + y * math.cos(a)
            x  = x2
            y  = y2
        if (d[0] == 'R'):
            a  = -d[1] * math.pi / 180 
            x2 = x * math.cos(a) - y * math.sin(a)
            y2 = x * math.sin(a) + y * math.cos(a)
            x  = x2
            y  = y2
        if (d[0] == 'F'):
            sx = sx + d[1] * x
            sy = sy + d[1] * y

    return int(abs(sx) + abs(sy) + 0.001)  


def solution(file):
    print("Input: ", file)

    lines = ut.read_lines(file)
    dirs = []
    for line in lines:
        dirs.append([line[0], int(line[1:])])

    p1 = part1(dirs)
    print("Part1: ", p1)

    p2 = part2(dirs)
    print("Part2: ", p2)


def main():
    solution("day12-test.txt");
    solution("day12-input.txt");


if __name__ == '__main__':
    main()
