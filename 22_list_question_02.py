#write a program to accept marks of 6 students and display them in a sorted manner

f1 = int(input("Enter marks of student 1:\n"))
f2 = int(input("Enter marks of student 2:\n"))
f3 = int(input("Enter marks of student 3:\n"))
f4 = int(input("Enter marks of student 4:\n"))
f5 = int(input("Enter marks of student 5:\n"))
f6 = int(input("Enter marks of student 6:\n"))

mylist = [f1,f2,f3,f4,f5,f6]
mylist.sort()
print(mylist)


