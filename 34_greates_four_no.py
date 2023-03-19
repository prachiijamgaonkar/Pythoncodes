#find the greatest number among four number and that number would be enter by user

n1=int(input("Enter number 1:\n"))
n2 = int(input("Enter number 2:\n"))
n3 = int(input("Enter number 3:\n"))
n4 = int(input("Enternumber 4:\n"))

if n1>n4:
    f1=n1
else:
    f1=n4

if n2>n3:
    f2=n2
else:
    f2=n3

if f1>f2:
    print("greater number is",f1)
else:
    print("Greater number is",f2)
