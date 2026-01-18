#find the 2nd largest element from the list.

user_input = input("enter numbers: ")

numbers = user_input.split()

for i in range(len(numbers)):
    numbers[i] = float(numbers[i])
    
if len(numbers) < 2:
    print("second largest number doesn't exist")
else:
    print()