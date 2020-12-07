import re

'striped fuchsia bags contain 2 shiny teal bags, 4 striped aqua bags, 4 dull lavender bags, 2 dull crimson bags.'

rules = {}
for line in open('aoc7-test.txt').readlines():
#for line in open('aoc7-input.txt').readlines():
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


# def allow_shiny_gold(rules, rule):
#     print(rule)
#     for inner in rules[rule]:
#         print(inner)
#         if inner[1] == 'shiny gold':
#             return True
#         else:
#             if allow_shiny_gold(rules, inner[1]): 
#                 return True
#     print()


def allow_shiny_gold(rules, rule):
    #print(rule, rules[rule])
    result = 0
    for inner in rules[rule]:
        if inner[1] == 'shiny gold':
            print(rule)
            result = 1
            return result
        else:
            result = allow_shiny_gold(rules, inner[1])
    return result
            

def contain_gold(rules, rule):
    for inner in rules[rule]:
        if inner[1] == 'shiny gold':
            return rule
    return None


sum = 0
for rule in rules:
#    sum += allow_shiny_gold(rules, rule)
    print(contain_gold(rules, rule))

