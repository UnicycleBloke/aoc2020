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

    # Set of all ingredients from all foods  
    ingredients = set()
    # Map of allergens to the set of ingredients they could be
    all_2_ings = {} 

    for f in foods:
        ingredients = ingredients.union(f.ings)
        for a in f.alls:
            if a in all_2_ings:
                all_2_ings[a] = all_2_ings[a].intersection(f.ings)
            else:
                all_2_ings[a] = set(f.ings)

    # Set of all ingredients which are allergens
    allergens  = set()
    for a in all_2_ings:
        allergens = allergens.union(all_2_ings[a])

    safe = ingredients.difference(allergens)
    print('Part1:', sum([len(safe.intersection(f.ings)) for f in foods]))


    # Map of ingredients identified as allergens
    ing_2_all = {}

    while True:
        found = False

        # Narrow down the set of ingredients that each allergen might be.
        for a in all_2_ings:
            ings = ingredients.copy()
            for f in foods:
                if a in f.alls:
                    ings = ings.intersection(f.ings)

            # We identified an allergen 
            if len(ings) == 1:
                ing_2_all[list(ings)[0]] = a
                found = True
                break

        # Remove the allergens that have been identified.
        for f in foods:
            for i in ing_2_all:
                f.ings = f.ings.difference(set([i]))
                f.alls = f.alls.difference(set([ing_2_all[i]])) 

        # We're done. This assumes we will always find an allergen. Not sure 
        # the constraints could be solved otherwise.
        if found == False: 
            break        

    pairs = [(k, ing_2_all[k]) for k in ing_2_all]
    print('Part2:', ','.join([x[0] for x in sorted(pairs, key=lambda x: x[1])]))


def main():
    solution("day21-test.txt")    
    solution("day21-input.txt")


if __name__ == '__main__':
    main()

