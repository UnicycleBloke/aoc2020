import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math
from functools import reduce


def part1b(data, cycles):
    alive = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                alive.add((i+50)*10000 + (j+50)*100 + 50)

    for s in range(cycles):
        neighbours = {}
        for c in alive:
            x = c // 10000
            y = (c // 100) % 100
            z = c % 100
            pos = [[i, j, k] for i in range(x-1, x+2) for j in range(y-1, y+2) for k in range(z-1, z+2)]
            for p in pos:
                if p[0] == x and p[1] == y and p[2] == z:
                    continue
                q = p[0]*10000 + p[1]*100 + p[2]
                if q in neighbours:
                    neighbours[q] = neighbours[q] + 1
                else:
                    neighbours[q] = 1

        alive2 = set()
        for c in neighbours:
            if c in alive and neighbours[c] in [2, 3]:
                alive2.add(c) 
            if c not in alive and neighbours[c] == 3:
                alive2.add(c) 
        alive = alive2
        print(s, len(alive))

    return len(alive) 


def part2b(data, cycles):
    alive = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                alive.add((i+50)*1000000 + (j+50)*10000 + 5000 + 50)

    for s in range(cycles):
        neighbours = {}
        for c in alive:
            x = (c // 1000000) % 100
            y = (c // 10000) % 100
            z = (c // 100) % 100
            w = (c) % 100
            pos = [[i, j, k, l] for i in range(x-1, x+2) for j in range(y-1, y+2) for k in range(z-1, z+2) for l in range(w-1, w+2)]
            for p in pos:
                if p[0] == x and p[1] == y and p[2] == z and p[3] == w:
                    continue
                q = p[0]*1000000 + p[1]*10000 + p[2]*100 + p[3]
                if q in neighbours:
                    neighbours[q] = neighbours[q] + 1
                else:
                    neighbours[q] = 1

        alive2 = set()
        for c in neighbours:
            if c in alive and neighbours[c] in [2, 3]:
                alive2.add(c) 
            if c not in alive and neighbours[c] == 3:
                alive2.add(c) 
        alive = alive2
        print(s, len(alive))

    return len(alive) 


def solution(file):
    print("Input: ", file)
    lines = ut.read_lines(file)

    p1 = part1b(lines, 6)
    print("Part1: ", p1)

    p2 = part2b(lines, 6)
    print("Part2: ", p2)


def main():
    solution("day17-test.txt")
    solution("day17-input.txt")


if __name__ == '__main__':
    main()

