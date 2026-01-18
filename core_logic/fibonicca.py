#Fibonacci using RECURSION

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("enter number of terms: "))

print("fibonacci series: ")

for i in range(terms):
    print(fibonacci(i), end=" ")