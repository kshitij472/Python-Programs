#program for counting vowels, consonants, digits, spaces.

text = input("enter string: ")             #for taking input from user

vowels = 0                                #starts the counts from 0 
consonants = 0
digits = 0
spaces = 0

vowel_set = "aeiouAEIOU"                  #created a list of vowels

for ch in text:                           #created loop for every character
    
    if ch == " ":                             #to check if the text has space in between
        spaces += 1
        
    elif ch.isdigit():                          #for digits 
        digits += 1
        
    elif ch.isalpha():                          #for alphabets
        
        if ch in vowel_set:                  # check whether the vowels are there or not
            vowels += 1
        else:
            consonants += 1
            
print("Vowels: ",vowels)                        #prints the final result 
print("consonants: ", consonants)
print("DIgits: ", digits)
print("Spaces: ", spaces)