n = int(input("enter numbers of term: "))
a = 0
b = 1

if n <=0:
    print("invalid")
elif n == 1:
    print(a)
else:
    print("fibonacci series: ")
    print(a, b, end=' ')

for i in range(2, n):
    c = a + b
    print(c,end=' ')
    a = b
    b = c