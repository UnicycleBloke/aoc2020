import sys
import os
import math
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


class Food:
    pass


def solution(file):
    print("Input:", file)
    data = ut.read_lines(file, True)
    foods = []
    for line in data:
        temp = line.replace('(contains', ':').replace(',', ' ').replace(')', ' ').strip().split(':')
        food = Food()
        food.ings = set(temp[0].split())
        food.alls = set(temp[1].split())
        foods.append(food)

    xxx_ingredients     = set.union(*[f.ings for f in foods])
    eng_allergens       = set.union(*[f.alls for f in foods])
    eng_all_to_xxx_ings = {a:set.intersection(*[f.ings for f in foods if a in f.alls]) for a in eng_allergens} 
    xxx_allergens       = set.union(*[eng_all_to_xxx_ings[a] for a in eng_allergens])

    # Part 1
    safe = xxx_ingredients.difference(xxx_allergens)
    print('Part1:', sum([len(safe.intersection(f.ings)) for f in foods]))

    # Part 2
    # Map of ingredients identified as allergens
    eng_all_to_ing = {}
    while True:
        # Find allergens which can be only one of the ingredients.
        pairs = {a:i for (a,i) in eng_all_to_xxx_ings.items() if len(i) == 1}
        # Assume zero or more matches.
        for p in pairs: 
            eng_all_to_ing[p] = list(pairs[p])[0] 
        # Zero means we're done - or the system of constraints can't be resolved. 
        if len(pairs) == 0: 
            break
        # Remove all the found ingredients from the food items for the next go around.
        ings = set.union(*[pairs[a] for a in pairs])        
        eng_all_to_xxx_ings = {a:i.difference(ings) for (a,i) in eng_all_to_xxx_ings.items()}

    print('Part2:', ','.join([i for i in sorted(eng_all_to_ing)]))
    print('Part2:', ','.join([eng_all_to_ing[i] for i in sorted(eng_all_to_ing)]))


def main():
    solution("day21-test.txt")    
    solution("day21-input.txt")


if __name__ == '__main__':
    main()

