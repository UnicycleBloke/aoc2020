import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math


primes = ut.read_primes()


def valid(fields, ticket):
    total = 0
    for i in ticket:
        valid = False
        for f in fields:
            if int(i) >= int(f[1]) and int(i) <= int(f[2]): valid = True
            if int(i) >= int(f[3]) and int(i) <= int(f[4]): valid = True
        if valid == False:
            total += int(i)
            #print(i)
    return total


def part1(fields, ticket, tickets):
    total = 0
    for t in tickets:
        total += valid(fields, t)
    return total


def field_valid_for_ticket(f, t, i):
    #print('Test', f, t, i)
    if int(t[i]) >= int(f[1]) and int(t[i]) <= int(f[2]): return True
    if int(t[i]) >= int(f[3]) and int(t[i]) <= int(f[4]): return True
    return False


def field_valid_for_tickets(f, ts, i):
    count = 0
    for t in ts:
        if field_valid_for_ticket(f, t, i) == True: count += 1
    return count


def part2(fields, ticket, tickets):
    good = []
    for t in tickets:
        if valid(fields, t) == 0:
            good.append(t)

    # Valid tickets
    for g in good:
        print(g)   
    print(len(good))

    # Fields with ranges
    for f in fields:
        print(f)   
    print(len(fields))     

    # Which fields match all valid tickets in position i
    # ERROR: Most positions have several matches
    # ERROR: Some positions have none
    rules = {}
    for i in range(len(ticket)):
        count = []
        for f in fields:
            if field_valid_for_tickets(f, good, i) == len(good):
                #rules[i] = f
                count.append(f[0])
                #break
        print(i, count)

    for r in rules:            
        print(r, rules[r])
    print(len(rules))     

    print(ticket, len(ticket))
    result = 1
    for r in rules:
        #print(r, rules[r], rules[r][0])
        if rules[r][0].startswith('departure'):
            #print(r, ticket[r])
            result = result * int(ticket[r])


    return result


def solution(file):
    print("Input: ", file)
    lines = ut.read_lines(file)

    i = 0
    # Rules
    fields = []
    while len(lines[i]) > 0:
        m = re.match('^(.*):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$', lines[i])
        if m == None:
            break 
        fields.append([m.group(x) for x in range(1, 6)])
        #print([m.group(x) for x in range(1, 6)])
        i += 1

    i += 1
    # Ticket
    ticket = lines[i].split(',')
    #print(ticket)
    i += 2

    # Tickets
    tickets = []
    while i < len(lines) > 0:
        tickets.append(lines[i].split(','))
        #print(lines[i].split(','))
        i += 1

    #p1 = part1(fields, ticket, tickets)
    #print("Part1: ", p1)

    p2 = part2(fields, ticket, tickets)
    print("Part2: ", p2)


def main():
    #solution("day16-test.txt")
    #solution("day16-test2.txt")
    solution("day16-input.txt")


if __name__ == '__main__':
    main()

