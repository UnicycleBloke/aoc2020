import re


def count_char(char, string):
    result = 0
    for c in string:
        if c == char:
            result += 1
    return result


lines = open('aoc2-input.txt').readlines()


num_ok  = 0
num_ok2 = 0
for line in lines:
    m = re.match('\s*(\d*)\s*-\s*(\d*)\s*(\w)\s*:\s*(\w*)', line)
    if m != None:
        min_ch = int(m.group(1))
        max_ch = int(m.group(2))

        # Part 1
        num_ch = count_char(m.group(3), m.group(4))
        if num_ch >= min_ch and num_ch <= max_ch:
            num_ok += 1

        # Part 2
        ch = m.group(3)
        pw = m.group(4)
        if pw[min_ch - 1] == ch and pw[max_ch - 1] != ch:
            num_ok2 += 1
        if pw[min_ch - 1] != ch and pw[max_ch - 1] == ch:
            num_ok2 += 1

        #print(m.group(0), m.group(1), m.group(2), m.group(3), m.group(4))
    else:
        raise "Boom"

print (num_ok, num_ok2)   



