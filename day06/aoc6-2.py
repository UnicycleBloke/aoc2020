
group  = []
groups = []

#for line in open('aoc6.txt').readlines():
for line in open('aoc6-input2.txt').readlines():
    line = line.strip()
    if len(line) > 0:
        group.append(line)
    else:
        groups.append(group)
        group = []

if len(group) > 0:
    groups.append(group)

#print (groups)

test = 'abcdefghijklmnopqrstuvwxyz'

total = 0
for g in groups:
    count = 0
    for c in test:
        num = 0
        for person in g:
            if c in person:
                num += 1
        if num == len(g):
            count += 1        
    total = total + count

print(total)
 