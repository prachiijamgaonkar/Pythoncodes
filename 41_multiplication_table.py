#Q1=>write a program to print multiplication table of a given no using for loop
num = int(input("Enter the number:\n"))

for i in range(0,11):
    print(str(i)+"X"+str(num) +"="+str(i*num) )


print(f"{num}x{i}={i*num}")#when we use f string we have to write variable as well as statement in curly braces and operator without curly braces


