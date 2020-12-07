import functools as ft

groups = ''.join(open('aoc6.txt').readlines()).replace('\n', ':').split('::')
q = set('abcdefghijklmnopqrstuvwzyz')
print(sum([len(set(g.replace(':', ''))) for g in groups]))
print(sum([len(ft.reduce(lambda a, b: a.intersection(b), [set(x) for x in g.split(':')], q)) for g in groups]))
print([sum([g.count(c) for c in q]) for g in groups])


groups = ''.join(open('aoc6-input2.txt').readlines()).replace('\n', ':').split('::')
q = set('abcdefghijklmnopqrstuvwzyz')
print(sum([len(set(g.replace(':', ''))) for g in groups]))
print(sum([len(ft.reduce(lambda a, b: a.intersection(b), [set(x) for x in g.split(':')], q)) for g in groups]))





