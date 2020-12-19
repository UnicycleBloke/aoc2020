import sys
import re


# Treat the BSP as a simple binary number
def pass_id(id_str):
    id = 0
    for ch in id_str:
        id = id * 2;
        if ch in ['B', 'R']:
            id += 1
    return id


def test_id(id_str, exp_id):
    id = pass_id(id_str)
    print(id_str, exp_id, id, 'Pass' if id == exp_id else '')


# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
test_id('BFFFBBFRRR', 567)
test_id('FFFBBBFRRR', 119)
test_id('BBFFBBFRLL', 820)
print()

max_id  = 0
all_ids = []
for line in open('aoc5-input.txt').readlines():
    id     = pass_id(line.strip())
    max_id = max(max_id, id)
    all_ids.append(id)

print('Part1:', max_id)    

for id in all_ids:
    if ((id + 1) not in all_ids) and ((id + 2) in all_ids):
        print('part2:', id + 1) 
