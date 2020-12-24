import sys
import os
import math
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


# Leave enough room for expansion of the circle of black.
SIZE = 200


def part1(rules):
    grid = [[0 for i in range(SIZE)] for j in range(SIZE)]

    black = 0
    for dirs in rules:
        x = SIZE // 2
        y = SIZE // 2
        for d in dirs:
            if d == 'nw':
                x = x - (y+1)%2 
                y = y + 1
            if d == 'ne':
                x = x + (y)%2 
                y = y + 1
            if d == 'sw':
                x = x - (y+1)%2 
                y = y - 1
            if d == 'se':
                x = x + (y)%2 
                y = y - 1
            if d == 'w':
                x = x - 1
            if d == 'e':
                x = x + 1

        bw = (grid[x][y] + 1) % 2
        if bw == 1: black += 1
        if bw == 0: black -= 1
        grid[x][y] = bw

    print(black)
    return [grid, black]


def neighbours(grid, x, y):
    num = 0
    # EW
    num = num + grid[x-1][y]
    num = num + grid[x+1][y]
    # N
    num = num + grid[x+0][y+1]
    if (y%2) == 1:
        num = num + grid[x+1][y+1]
    else:
        num = num + grid[x-1][y+1]
    # S
    num = num + grid[x+0][y-1]
    if (y%2) == 1:
        num = num + grid[x+1][y-1]
    else:
        num = num + grid[x-1][y-1]
    return num


# def min_max(grid):
#     minx = SIZE
#     miny = SIZE
#     maxx  = 0
#     maxy  = 0
#     for x in range(1, SIZE - 1):
#         for y in range(1, SIZE - 1):
#             if grid[x][y] == 1:
#                 minx = min(minx, x)
#                 miny = min(miny, y)
#                 maxx = max(maxx, x)
#                 maxy = max(maxy, y)
#     print('min({}, {}) max({}, {})'.format(minx, miny, maxx, maxy))


def part2(grid, count):
    for day in range(100):
        flip = [[0 for i in range(SIZE)] for j in range(SIZE)]
        for x in range(1, SIZE - 1):
            for y in range(1, SIZE - 1):
                flip[x][y] = neighbours(grid, x, y)

        for x in range(1, SIZE - 1):
            for y in range(1, SIZE - 1):
                # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
                if grid[x][y] == 1:
                    if flip[x][y] == 0 or flip[x][y] > 2:
                        grid[x][y] = 0
                        count -= 1
                # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
                elif grid[x][y] == 0:
                    if flip[x][y] == 2:
                        grid[x][y] = 1
                        count += 1

        #min_max(grid)
        print('Day {}: {}'.format(day + 1, count))


def solution(file):
    print("Input:", file)
    data = ut.read_lines(file, True)

    rules = []
    for d in data:
        i    = 0
        dirs = []
   
        while i < len(d):
            if d[i:i+2] == 'nw':
                dirs.append('nw')
                i += 2
            if d[i:i+2] == 'ne':
                dirs.append('ne')
                i += 2
            if d[i:i+2] == 'sw':
                dirs.append('sw')
                i += 2
            if d[i:i+2] == 'se':
                dirs.append('se')
                i += 2
            if d[i:i+1] == 'w':
                dirs.append('w')
                i += 1
            if d[i:i+1] == 'e':
                dirs.append('e')
                i += 1
        rules.append(dirs)

    p1 = part1(rules)
    part2(p1[0], p1[1])


def main():
    solution("day24-test.txt")    
    solution("day24-input.txt")


if __name__ == '__main__':
    main()
