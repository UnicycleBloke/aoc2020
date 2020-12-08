import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


def part1():
    print('Part1:')


def part2():
    print('Part2:')


def main():
    if len(sys.argv) < 2:
        print('Provide input file name')
        exit(-1)

    #lines = ut.read_groups(sys.argv[1])
    lines = ut.read_lines(sys.argv[1])
    for line in lines:
        print(line)

    part1()
    part2()   


if __name__ == '__main__':
    main()
