import sys

char_frequency = dict()

try:
    with open(sys.argv[1], "r") as file:
        words = file.read()
        for char in words:
            char = char.lower()
            if char.isalpha:
                char_frequency[char] = char_frequency.get(char,0)+1


    for key,value in char_frequency.items():
        print(key,value)
except FileNotFoundError:
    print("This file doesn't exist") 