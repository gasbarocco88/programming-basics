import sys

try:
    output = ""
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        for line in lines[:10]:
            print(line, end='')
except FileNotFoundError:
    print("This file doesn't exist") 