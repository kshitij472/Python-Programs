#program for counting vowels, consonants, digits, spaces.

text = input("enter string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

vowel_set = "aeiouAEIOU"

for ch in text:
    
    if ch == " ":
        spaces += 1
        
    elif ch.isdigit():
        digits += 1
        
    elif ch.isalpha():
        
        if ch in vowel_set:
            vowels += 1
        else:
            consonants += 1
            
print("Vowels: ",vowels)
print("consonants: ", consonants)
print("DIgits: ", digits)
print("Spaces: ", spaces)