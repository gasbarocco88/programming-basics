"""There is at least one word in the English language that contains each of the vowels A, E, I, O, U and Y exactly once and in order. 

Write a program that searches a file containing a list of words and displays all of the words that meet this constraint. 
"""

try:
    vowels = ["a","e","i","o","u","y"]
    word_list = []
    counter = 0

    with open(r"D:\coding\tomorrowdevs\program basic exercise\programming-basics\projects\m4\006-two-word-random-password\solutions\RoccoFigliamonti\englishwords.txt") as f:
        words = f.read().split()
        for word in words:
            for char in word:
                if char.lower() == vowels[counter]:
                    counter += 1
                if counter == len(vowels):
                    word_list.append(word)
            counter = 0
    
    print(word_list)

except FileNotFoundError:
    print("This file doesn't exist") 
