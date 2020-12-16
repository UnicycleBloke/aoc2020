import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math
from functools import reduce

def invalid_sum(fields, ticket, extra):
    total = 0
    for p in ticket:
        valid = False
        for f in fields:
            if p >= f[1] and p <= f[2]: valid = True
            if p >= f[3] and p <= f[4]: valid = True
        if valid == False:
            total += (p + extra)
            # Perfect for Part 1, massive bug in Part 2 due to 0 
            # value in some ticket being invalid. So add on an extra bit to fix.
            #total += p
    return total


def field_match(f, p):
    if p >= f[1] and p <= f[2]: return True
    if p >= f[3] and p <= f[4]: return True
    return False


def part1(fields, ticket, tickets):
    total = 0
    for t in tickets:
        total += invalid_sum(fields, t, 0)
    return total


def part2(fields, ticket, tickets):
    valid_tickets = [t for t in tickets if invalid_sum(fields, t, 1) == 0]

    # For each field, find the set of positions for which it matches all 
    # valid tickets - this is a rule
    rules = []
    for f in fields:
        # The field potentially matches all positions for all tickets
        positions = {p for p in range(len(ticket))}
        for t in valid_tickets:
            # Only some positions match this field for this ticket
            match = {p for p in range(len(ticket)) if field_match(f, t[p]) == True }
            positions = positions.intersection(match)
        rules.append(positions)

    # Iterate to find the positions for each field - if the rule has 
    # one entry, that is a match.
    result  = 1
    result2 = set()
    found   = set()
    for k in range(len(ticket)):
        for i in range(len(rules)):
            if len(rules[i]) == 1:
                if fields[i][0].startswith('departure'):
                    p = list(rules[i])[0]
                    result = result * ticket[p]
                    result2.add(p)
                    #print(k, p, ticket[p], fields[i][0], result, result2)
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

