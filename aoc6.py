
group  = ''
groups = []

for line in open('aoc6-input2.txt').readlines():
    line = line.strip()
    if len(line) > 0:
        group = group + line
    else:
        groups.append(group)
        group = ''

if len(group) > 0:
    groups.append(group)

#print (groups)

test = 'abcdefghijklmnopqrstuvwxyz'

total = 0
for g in groups:
    count = 0
    for c in test:
        if c in g:
            count += 1
    print (count)
    total = total + count
print(total)
 