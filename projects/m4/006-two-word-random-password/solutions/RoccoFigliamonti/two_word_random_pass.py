"""
Write a program that reads a file containing a list of words, randomly selects two
of them, and concatenates them to produce a new password. 

When producing the password ensure that the total length is between 8 and 10 characters, and that each word used is at least three letters long. 

Capitalize each word in the password so that the user can easily see where one word ends and the next one begins. 

Finally, your program should display the password for the user."""

from random import choice

try:
    with open(r"D:\coding\tomorrowdevs\program basic exercise\programming-basics\projects\m4\006-two-word-random-password\solutions\RoccoFigliamonti\englishwords.txt") as f:
        words = f.read().split()
        word1 = ""
        word2 = ""
        while not (len(word1)>2 and len(word1)<8):
            word1 = choice(words).capitalize()
        while not (len(word2)>2 and len(word1+word2)>=8 and len(word1+word2)<=10 ):
            word2 = choice(words).capitalize()

        password = word1 + word2
        print(password)
        print(len(password))

except FileNotFoundError:
    print("This file doesn't exist") 
