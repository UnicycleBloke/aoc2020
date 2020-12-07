import re

'striped fuchsia bags contain 2 shiny teal bags, 4 striped aqua bags, 4 dull lavender bags, 2 dull crimson bags.'

rules = {}
#for line in open('aoc7-test.txt').readlines():
for line in open('aoc7-input.txt').readlines():
    line = line.strip()
    line = line.replace('bags', ':')
    line = line.replace('bag', ':')
    line = line.replace('contains', ':')
    line = line.replace('contain', ':')
    line = line.replace(',', '')
    line = line.replace('.', '')
    data = [x.strip() for x in line.split(':')]
    #print(data)
    
    b = []
    for item in data[1:]:
        m = re.match('^(\d+)\s(.+)$', item)
        if m != None:
            b.append([int(m.group(1)), m.group(2)])
    rules[data[0]] = b

#print(rules)  


def contain_gold(rules, rule, indent):
    print(' ' * indent, rule)
    for inner in rules[rule]:
        if inner[1] == 'shiny gold':
            print(' ' * (indent + 4), 'YYYY')
            return True
        else:
            if contain_gold(rules, inner[1], indent + 4) == True:
                return True
    print(' ' * (indent + 4), 'NNNN')
    return False


def how_many(rules, rule, indent):
    sum = 0
    print(' ' * indent, rule)
    indent += 4
    for inner in rules[rule]:
        print(' ' * indent, inner[1], inner[0])
        sum += inner[0]
        sum += inner[0] * how_many(rules, inner[1], indent + 4)
    return sum



# sum = 0
# for rule in rules:
#     if contain_gold(rules, rule, 4):
#         sum += 1

# print(sum)

print(how_many(rules, 'shiny gold', 4))


