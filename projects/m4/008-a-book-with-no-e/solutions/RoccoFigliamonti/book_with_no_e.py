"""
Write a program that reads a list of words from a file and determines what propor-
tion of the words use each letter of the alphabet. 

Display this result for all 26 letters and include an additional message that identifies the letter that is used in the smallest proportion of the words. 

Your program should ignore any punctuation marks that are present in the file and it should treat uppercase and lowercase letters as equivalent.
		 """



letter_count = {}
reverse_letter_count = {}

try:
    with open(r"D:\coding\tomorrowdevs\program basic exercise\programming-basics\projects\m4\005-words-that-occur-most\solutions\RoccoFigliamonti\poem.txt") as f:
        words = f.read().split()
        for word in words:
            for char in word:
                if char.isalpha():
                    letter_count[char.lower()] = letter_count.get(char.lower(),0)+1
    
    for k,v in letter_count.items():
        reverse_letter_count[v] = reverse_letter_count.get(v, []) + [k]
    for k,v in sorted(reverse_letter_count.items()):
        print(k,v)
    
except FileNotFoundError:
    print("This file doesn't exist") 
