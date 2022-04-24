"""
Write a program that displays the word (or words) that occur most frequently in a file. 

Each line will need to be split into words, and any leading or trailing punctuation marks will need to be removed from each word. 

Your program should also ignore capitalization when counting how many times each word occurs.
"""
import string

string.punctuation
try:
    word_dictionary = dict()
    with open(r"D:\coding\tomorrowdevs\program basic exercise\programming-basics\projects\m4\005-words-that-occur-most\solutions\RoccoFigliamonti\poem.txt") as f:
        words = f.read().split()
        #manipulate every word to remove punctuation and create a dictionary with the frequency of every word
        for word in words:
            new_word = "".join(ch for ch in word if ch not in set(string.punctuation)).lower()
            word_dictionary[new_word] = word_dictionary.get(new_word,0) + 1
    
    #reverse key-value in dict to have the frequency as key
    reverse_word_dictionary = {}
    for k, v in word_dictionary.items():
        reverse_word_dictionary[v] = reverse_word_dictionary.get(v, []) + [k]
    
    #sorting in discending frequency
    reverse_word_dictionary = sorted(reverse_word_dictionary.items(), reverse=True)
    for k,v in reverse_word_dictionary:
        print(k,v)

except FileNotFoundError:
    print("This file doesn't exist") 
