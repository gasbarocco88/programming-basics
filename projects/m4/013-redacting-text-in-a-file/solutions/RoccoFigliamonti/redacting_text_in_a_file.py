import string


#creating the list of sensitive words from a file
try:
    with open(r"D:\coding\tomorrowdevs\program basic exercise\programming-basics\projects\m4\013-redacting-text-in-a-file\solutions\RoccoFigliamonti\words.txt", "r") as file:
        reserved_words_list = file.read().split(",")
except FileNotFoundError:
    print("This file doesn't exist") 

print(reserved_words_list)

#reading the input file and write a new file without sensitive words
try:
    with open(r"D:\coding\tomorrowdevs\program basic exercise\programming-basics\projects\m4\013-redacting-text-in-a-file\solutions\RoccoFigliamonti\text.txt", "r") as file_input, \
    open(r"D:\coding\tomorrowdevs\program basic exercise\programming-basics\projects\m4\013-redacting-text-in-a-file\solutions\RoccoFigliamonti\text_output.txt", "w") as file_output:
        lines = file_input.readlines()
        for line in lines:
            for word in line.split(): #control every word in the old file
                new_word = "".join(ch for ch in word if ch not in set(string.punctuation)).lower() #eliminate punct and formatting
                if new_word in reserved_words_list:
                    line = line.replace(word,"****") #replace the single word in asterics
            file_output.write(line) 
except FileNotFoundError:
    print("This file doesn't exist") 
