import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


def pack1(rows):
    rows2 = []
    for row in rows:
        rows2.append(row[:])

    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[0]) - 1):
            cells = [x for x in rows[r][c-1:c+2]] + [x for x in rows[r-1][c-1:c+2]] + [x for x in rows[r+1][c-1:c+2]]
            occ   = len([x for x in cells if x == '#'])
            if (occ == 0) and (rows[r][c] == 'L'):
                rows2[r][c] = '#'
            elif (occ >= 5) and (rows[r][c] == '#'):
                rows2[r][c] = 'L'

    return rows2


def see(rows, r, c, rdel, cdel):
    while True:
        r += rdel
        if r == 0 or r == (len(rows) - 1):
            return 0 
        c += cdel
        if c == 0 or c == (len(rows[0]) - 1):
            return 0 
        if rows[r][c] == '#':
            return 1
        if rows[r][c] == 'L':
            return 0
    return 0


def pack2(rows):
    rows2 = []
    for row in rows:
        rows2.append(row[:])

    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[0]) - 1):
            occ  = 0
            occ += see(rows, r, c,  1, 1)
            occ += see(rows, r, c,  0, 1)
            occ += see(rows, r, c, -1, 1)
            occ += see(rows, r, c,  1, 0)
            #occ += see(rows, r, c,  0, 0)
            occ += see(rows, r, c, -1, 0)
            occ += see(rows, r, c,  1, -1)
            occ += see(rows, r, c,  0, -1)
            occ += see(rows, r, c, -1, -1)

            if (occ == 0) and (rows[r][c] == 'L'):
                rows2[r][c] = '#'
            elif (occ >= 5) and (rows[r][c] == '#'):
                rows2[r][c] = 'L'

    return rows2


def changes(rows, rows2):
    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[0]) - 1):
            if rows[r][c] != rows2[r][c]:
                return True
    return False


def occupied(rows):
    occ = 0
    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[0]) - 1):
            if rows[r][c] == '#':
                occ += 1
    return occ


def part1(rows):    
    rows2 = pack1(rows)
    while changes(rows, rows2) == True:
        rows = rows2
        rows2 = pack1(rows)
    return occupied(rows2)


def part2(rows): 
    rows2 = pack2(rows)
    while changes(rows, rows2) == True:
        rows = rows2
        rows2 = pack2(rows)
    return occupied(rows2)


def solution(file):
    print("Input: ", file)

    lines = ut.read_lines(file)
    rows = []
    rows.append(list('.' * (len(lines[0]) + 2)))
    for line in lines:
        rows.append(list('.' + line + '.'))
    rows.append(list('.' * (len(lines[0]) + 2)))

    p1 = part1(rows)
    print("Part1: ", p1)

    p2 = part2(rows)
    print("Part2: ", p2)


def main():
    solution("day11-test.txt");
    solution("day11-input.txt");


if __name__ == '__main__':
    main()

