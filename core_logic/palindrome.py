
#Program to check wheter a string is palindrome or not

text = input("enter a string: ")

is_palindrome = True
start = 0          #it starts from string's 1st letter 
end = len(text) - 1      #end from last 

while start < end:
    if text[start] != text[end]:       #to compare the right side and left side's char
        is_palindrome = False                    #if both side charcters are not same then it will tell that it is not palindrome
        break                                      #and break the code
    start += 1
    end -= 1
if is_palindrome:
    print("It is a palindrome")
else:
    print("is not a palindrome")
