#!/bin/Python3

import sys 

def generate_leetspeak_combinations(word):
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

    def backtrack(curr_word, index):
        if index == len(word):
            combinations.append(curr_word)
            return
        for char in leet_characters.get(word[index], [word[index]]):
            backtrack(curr_word + char, index + 1)

    combinations = []
    backtrack('', 0)
    return combinations

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 LeetSpeak.py <word>")
        sys.exit(1)

    # Get the word from command-line argument
    word = sys.argv[1]

# Generate leetspeak combinations
combinations = generate_leetspeak_combinations(word.upper())

# Print the generated combinations
for combo in combinations:
    print(combo)

