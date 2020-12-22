import sys
import os
import math
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


def score(deck):
    return sum(deck[i]*(len(deck)-i) for i in range(len(deck)))


# Create huge number as a simple hash of the state of the deck.
# Probably much better methods...
def deck_hash(deck):
    return sum(deck[i]*(100**i) for i in range(len(deck))) * 100 + len(deck)


game_counter = 0


def post_game(deck1, deck2, game):
    if game == 1 and (len(deck1) == 0 or len(deck2) == 0):
        #print()
        #print("== Post-game results ==")
        #print("Player 1's deck:", ', '.join([str(c) for c in deck1]))
        #print("Player 2's deck:", ', '.join([str(c) for c in deck2]))
        winner_score = max(score(deck1), score(deck2))
        #print("Winner's score:", winner_score)
        print("Part2:", winner_score)


def recursive_combat(deck1, deck2):
    global game_counter
    game_counter += 1
    game = game_counter

    #print('=== Game {} ==='.format(game))
    #print()

    scores1 = []
    scores2 = []
    rounds  = 1

    while True:
        #print('-- Round {} (Game {}) --'.format(rounds, game))
        #print("Player 1's deck:", ', '.join([str(c) for c in deck1]))
        #print("Player 2's deck:", ', '.join([str(c) for c in deck2]))

        # Prevent recursion - Player 1 wins 
        s1 = deck_hash(deck1)      
        s2 = deck_hash(deck2)       
        if s1 in scores1 or s2 in scores2:
            return 1
        scores1.append(s1)        
        scores2.append(s2)   

        c1 = deck1[0]
        c2 = deck2[0]
        #print("Player 1 plays:", c1)
        #print("Player 2 plays:", c2)

        if len(deck1) > c1 and len(deck2) > c2:
            #print("Playing a sub-game to determine the winner...")
            #print()
            winner = recursive_combat(deck1[1:c1+1], deck2[1:c2+1])
            #print("...anyway, back to game {}.".format(game))
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            #print("Player 1 wins round {} of game {}!".format(rounds, game))
            deck1 = deck1[1:] + [c1, c2]
            deck2 = deck2[1:]
        else:
            #print("Player 2 wins round {} of game {}!".format(rounds, game))
            deck1 = deck1[1:]
            deck2 = deck2[1:] + [c2, c1]

        if len(deck1) == 0:
            #print("The winner of game {} is player 2!".format(game))
            #print()
            post_game(deck1, deck2, game)
            return 2          
        elif len(deck2) == 0:
            #print("The winner of game {} is player 1!".format(game))
            #print()
            post_game(deck1, deck2, game)
            return 1

        rounds += 1
        #print()     


def part1(deck1, deck2):
    while True:
        if len(deck1) == 0 or len(deck2) == 0:
            break

        c1 = deck1[0]
        c2 = deck2[0]
        if c1 > c2:
            deck1 = deck1[1:] + [c1, c2]
            deck2 = deck2[1:]
        else:
            deck1 = deck1[1:]
            deck2 = deck2[1:] + [c2, c1]

    print("Part1: ", max(score(deck1), score(deck2)))    


def part2(deck1, deck2):
    global game_counter
    game_counter = 0
    recursive_combat(deck1[:], deck2[:])


def solution(file):
    print("Input:", file)
    data = ut.read_lines(file, True)

    deck1 = []
    i = 1
    while i < len(data):
        if len(data[i]) == 0:
            break
        deck1.append(int(data[i]))
        i += 1

    deck2 = []
    i = i + 2
    while i < len(data):
        if len(data[i]) == 0:
            break
        deck2.append(int(data[i]))
        i += 1

    part1(deck1[:], deck2[:])
    part2(deck1[:], deck2[:])


def main():
    solution("day22-test.txt")    
    solution("day22-input.txt")


if __name__ == '__main__':
    main()
