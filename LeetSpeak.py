#!/bin/Python3

import sys
from itertools import product

def generate_leetspeak_combinations(word):

# UpperLower List
    if diff == "UpperLower":
        leet_characters = {
            'A': ['a', 'A'],
            'B': ['b', 'B'],
            'C': ['c', 'C'],
            'D': ['d', 'D'],
            'E': ['e', 'E'],
            'F': ['f', 'F'],
            'G': ['g', 'G'],
            'H': ['h', 'H'],
            'I': ['i', 'I'],
            'J': ['j', 'J'],
            'K': ['k', 'K'],
            'L': ['l', 'L'],
            'M': ['m', 'M'],
            'N': ['n', 'N'],
            'O': ['o', 'O'],
            'P': ['p', 'P'],
            'Q': ['q', 'Q'],
            'R': ['r', 'R'],
            'S': ['s', 'S'],
            'T': ['t', 'T'],
            'U': ['u', 'U'],
            'V': ['v', 'V'],
            'W': ['w', 'W'],
            'X': ['x', 'X'],
            'Y': ['y', 'Y'],
            'Z': ['z', 'Z']
        }

# Easy List
    elif diff == "Easy":
        leet_characters = {
            'A': ['a', 'A', '4', '@'],
            'B': ['b', 'B', '8', '13'],
            'C': ['c', 'C', '('],
            'D': ['d', 'D'],
            'E': ['e', 'E', '3'],
            'F': ['f', 'F'],
            'G': ['g', 'G', '6', '9'],
            'H': ['h', 'H', '#'],
            'I': ['i', 'I', '1', '!'],
            'J': ['j', 'J'],
            'K': ['k', 'K'],
            'L': ['l', 'L', '1', '!'],
            'M': ['m', 'M'],
            'N': ['n', 'N'],
            'O': ['o', 'O', '0'],
            'P': ['p', 'P'],
            'Q': ['q', 'Q', '9'],
            'R': ['r', 'R'],
            'S': ['s', 'S', '5', '$'],
            'T': ['t', 'T', '7', '+'],
            'U': ['u', 'U'],
            'V': ['v', 'V'],
            'W': ['w', 'W'],
            'X': ['x', 'X'],
            'Y': ['y', 'Y'],
            'Z': ['z', 'Z', '2']
        }

# Medium List
    elif diff == "Medium":
        leet_characters = {
        'A': ['a', 'A', '4', '@'],
            'B': ['b', 'B', '8', '13'],
            'C': ['c', 'C', '(', '<', '{'],
            'D': ['d', 'D', '|)', '|>'],
            'E': ['e', 'E', '3'],
            'F': ['f', 'F', '|=', 'ph'],
            'G': ['g', 'G', '6', '9'],
            'H': ['h', 'H', '#'],
            'I': ['i', 'I', '1', '!', '|'],
            'J': ['j', 'J'],
            'K': ['k', 'K'],
            'L': ['l', 'L', '|_', '|', '£'],
            'M': ['m', 'M'],
            'N': ['n', 'N'],
            'O': ['o', 'O', '0'],
            'P': ['p', 'P'],
            'Q': ['q', 'Q', '9'],
            'R': ['r', 'R'],
            'S': ['s', 'S', '5', '$'],
            'T': ['t', 'T', '7', '+'],
            'U': ['u', 'U'],
            'V': ['v', 'V'],
            'W': ['w', 'W'],
            'X': ['x', 'X'],
            'Y': ['y', 'Y'],
            'Z': ['z', 'Z', '2']
        }

# Hard List
    elif diff == 'Hard':
        leet_characters = {
            'A': ['a', 'A', '4', '@', '/-\\'],
            'B': ['b', 'B', '8', '13', '|3'],
            'C': ['c', 'C', '(', '<', '{'],
            'D': ['d', 'D', '|)', '|>'],
            'E': ['e', 'E', '3', '€', '[-'],
            'F': ['f', 'F', '|=', 'ph'],
            'G': ['g', 'G', '6', '9', '(_+'],
            'H': ['h', 'H', '#', '|-|', '|-|'],
            'I': ['i', 'I', '1', '!', '|'],
            'J': ['j', 'J', '_|', '_/', '¿'],
            'K': ['k', 'K', '|<', '|{'],
            'L': ['l', 'L', '|_', '|', '£'],
            'M': ['m', 'M', '|\\/|', '/\\/\\'],
            'N': ['n', 'N', '|\\|', '/\\/'],
            'O': ['o', 'O', '0', '()', '[]'],
            'P': ['p', 'P', '|°', '|>', '|*'],
            'Q': ['q', 'Q', '9', '0_', '(,)'],
            'R': ['r', 'R', '|2', '|?', '|2'],
            'S': ['s', 'S', '5', '$', '§'],
            'T': ['t', 'T', '7', '+', '†'],
            'U': ['u', 'U', '|_|', 'µ', '(_)'],
            'V': ['v', 'V', '\\/',],
            'W': ['w', 'W', '\\/\\/', '\\^/', '|/\\|'],
            'X': ['x', 'X', '><', '}{', ']['],
            'Y': ['y', 'Y', '¥', '`/'],
            'Z': ['z', 'Z', '2', '7_', '%']
        }
    
    else:
        print("error")


    # Find total amount of combinations
    total_combinations = 1
    for char in word:
        total_combinations *= len(leet_characters.get(char, [char]))
    m = int(total_combinations / 5)

    # Create LeetSpeak combinations
    def backtrack(curr_word, index):
        if index == len(word):
            combinations.append(curr_word)
            return
        for char in leet_characters.get(word[index], [word[index]]):
            backtrack(curr_word + char, index + 1)

    # Progress bar and return combo list
    combinations = []
    backtrack('',0)
    return combinations

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python3 LeetSpeak.py <word> <UL/E/M/H> <Progbar On/Off>")
        sys.exit(1)

    # Get the word from command-line argument
    word = sys.argv[1]
    diff = sys.argv[2]
    prog = sys.argv[3]
    
# Generate leetspeak combinations
combinations = generate_leetspeak_combinations(word.upper())

# Print the generated combinations
for combo in combinations:
    print(combo)

