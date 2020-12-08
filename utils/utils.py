import sys
import re


# Read individual lines from a file, optionally preserving blanks
def read_lines(filename, allow_blanks = False):
    return [l.strip() for l in open(filename).readlines() if len(l.strip()) > 0 or allow_blanks]

# Concatenate consecutive lines from a file, using blanks as delimiters
# Assume only single blank lines in the input - true so far
def read_groups(filename, delim = ':', space = ':'):
    lines  = read_lines(filename, True)
    groups = []
    group  = ''
    for line in lines:
        if len(line) > 0:
            group = group + line + ' '
        else:
           if len(group) > 0:
               groups.append(group)
               group = ''

    if len(group) > 0:
        groups.append(group)

    return groups


