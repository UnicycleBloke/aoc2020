import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math
from functools import reduce


def field_match(field, value):
    if value >= field[1] and value <= field[2]: return True
    if value >= field[3] and value <= field[4]: return True
    return False


def invalid_sum(fields, ticket, extra):
    return sum([(p + extra) for p in ticket if not any(field_match(f, p) for f in fields)])


def part1(fields, ticket, tickets):
    return sum([invalid_sum(fields, t, 0) for t in tickets])


def part2(fields, ticket, tickets):
    valid_tickets = [t for t in tickets if invalid_sum(fields, t, 1) == 0]

    # For each field, find the set of positions for which it matches all valid tickets
    rules = []
    for f in fields:
        positions = {p for p in range(len(ticket))}
        for t in valid_tickets:
            match = {p for p in range(len(ticket)) if field_match(f, t[p]) == True }
            positions = positions.intersection(match)
        rules.append(positions)

    # Iterate to find the positions for each field - if the rule has 
    # one entry, that is a match.
    result  = 1
    found   = set()
    for k in range(len(ticket)):
        for i in range(len(rules)):
            if len(rules[i]) == 1:
                if fields[i][0].startswith('departure'):
                    result = result * ticket[list(rules[i])[0]]
                found = found.union(rules[i]) 
        for j in range(len(rules)):
            rules[j] = rules[j] - found

    return result


def solution(file):
    print("Input: ", file)
    lines = ut.read_lines(file)

    i = 0
    fields = []
    while len(lines[i]) > 0:
        m = re.match('^(.*):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$', lines[i])
        if m == None:
            break 
        field = [m.group(1)] + [int(m.group(x)) for x in range(2, 6)]
        fields.append(field)
        i += 1

    i += 1
    ticket = [int(x) for x in lines[i].split(',')]
    i += 2

    tickets = []
    while i < len(lines) > 0:
        tickets.append([int(x) for x in lines[i].split(',')])
        i += 1

    p1 = part1(fields, ticket, tickets)
    print("Part1: ", p1)
    p2 = part2(fields, ticket, tickets)
    print("Part2: ", p2)


def main():
    solution("day16-input.txt")


if __name__ == '__main__':
    main()

