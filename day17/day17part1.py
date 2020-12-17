import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math
from functools import reduce


def get_active(grid, i, j, k):
    num = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            for dk in range(-1, 2):
                if grid[i+di][j+dj][k+dk] == '#':
                    num += 1

    act  = 1 if grid[i][j][k] == '#' else 0
    num -= act 
    return [act, num]


def run(grid, num):
    grid2 = [[['.' for k in range(num)] for j in range(num)] for i in range(num)]
    for i in range(1, num-1):
        for j in range(1, num-1):
            for k in range(1, num-1):
                act = get_active(grid, i, j, k)
                if (act[0] == 1) and (act[1] == 2 or act[1] == 3):
                    grid2[i][j][k] = '#'
                if (act[0] == 0) and (act[1] == 3): 
                    grid2[i][j][k] = '#'
    return grid2


def count_active(grid, num):
    count = 0
    for i in range(1, num-1):
        for j in range(1, num-1):
            for k in range(1, num-1):
                if grid[i][j][k] == '#':
                    count += 1
    return count


def part1(data, cycles):
    num  = (len(data) + (cycles + 3) * 2) 
    off  = num // 2 - 1

    grid = [[['.' for k in range(num)] for j in range(num)] for i in range(num)]
    for i in range(len(data)):
        for j in range(len(data[i])):
            grid[off][i+off][j+off] = data[i][j]

    for c in range(cycles):
        grid = run(grid, num)

    return count_active(grid, num)


def solution(file):
    print("Input: ", file)
    p1 = part1(ut.read_lines(file), 6)
    print("Part1: ", p1)


def main():
    solution("day17-test.txt")
    solution("day17-input.txt")


if __name__ == '__main__':
    main()

