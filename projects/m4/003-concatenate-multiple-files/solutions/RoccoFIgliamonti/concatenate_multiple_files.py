import sys

try:
    for file in sys.argv[1:]:
        with open(file, "r") as file:
            for line in file:
                print(line.rstrip())
except FileNotFoundError:
    print("This file doesn't exist") 