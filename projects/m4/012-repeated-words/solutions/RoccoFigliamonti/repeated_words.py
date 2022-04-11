"""
In this exercise you will write a program that detects repeated words in a text file. When a repeated word is found your program should display a message that contains the line number and the repeated word.

 Ensure that your program correctly handles the case where the same word appears at the end of one line and the beginning of the following line, as shown in the previous example. 
 
 The name of the file to examine will be provided as the program’s only command line argument."""

import string
 
#list.index()

try:
    with open("D:\\coding\\tomorrowdevs\\program basic exercise\\programming-basics\\projects\\m4\\012-repeated-words\\solutions\\RoccoFigliamonti\\ciao.txt") as f:
        lines = f.readlines()
        new_lines = []
        # create new document with only lower char and without punctuation
        # line by line and word by word
        for line in lines:
            for word in line.split():
                new_word = "".join(ch for ch in word if ch not in set(string.punctuation)).lower()
                line = line.replace(word,new_word)
            new_lines.append(line) #new list of lines with modified words
        
        # control repeated words inside the same line: split every line into words and see if two consecutive are equal
        for line in new_lines:
            for i in range(len(line.split())-1): 
                if line.split()[i] == line.split()[i+1]: 
                    print(f"Repeated word: {line.split()[i]} \nline: {new_lines.index(line)+1}")

        # control repeated words between different lines: last word of the each line has to be equal of first word of the next line
        for i in range(len(new_lines)-1):            
            if new_lines[i].split()[-1] == new_lines[i+1].split()[0]:
                print(f"Repeated word: {new_lines[i].split()[-1]} \nline: {i+1} ")
              


except FileNotFoundError:
    print("This file doesn't exist") 
