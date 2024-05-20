#!/bin/Python3

import sys 

def generate_leetspeak_combinations(word):
    leet_characters = {
        'A': ['A', 'a', '4', '@', '/-\\'],
        'B': ['B', 'b', '8', '13', '|3'],
        'C': ['C', 'c', '(', '<', '{'],
        'D': ['D', 'd', '|)', '|>'],
        'E': ['E', 'e', '3', '€', '[-'],
        'F': ['F', 'f', '|=', 'ph'],
        'G': ['G', 'g', '6', '9', '(_+'],
        'H': ['H', 'h', '#', '|-|', '|-|'],
        'I': ['I', 'i', '1', '!', '|'],
        'J': ['J', 'j', '_|', '_/', '¿'],
        'K': ['K', 'k', '|<', '|{'],
        'L': ['L', 'l', '|_', '|', '£'],
        'M': ['M', 'm', '|\\/|', '/\\/\\'],
        'N': ['N', 'n', '|\\|', '/\\/'],
        'O': ['O', 'o', '0', '()', '[]'],
        'P': ['P', 'p', '|°', '|>', '|*'],
        'Q': ['Q', 'q', '9', '0_', '(,)'],
        'R': ['R', 'r', '|2', '|?', '|2'],
        'S': ['S', 's', '5', '$', '§'],
        'T': ['T', 't', '7', '+', '†'],
        'U': ['U', 'u', '|_|', 'µ', '(_)'],
        'V': ['V', 'v', '\\/',],
        'W': ['W', 'w', '\\/\\/', '\\^/', '|/\\|'],
        'X': ['X', 'x', '><', '}{', ']['],
        'Y': ['Y', 'y', '¥', '`/'],
        'Z': ['Z', 'z', '2', '7_', '%']
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

