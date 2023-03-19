#Q3=>  Write a program to find out whether a student is pass or fail,if it requires total 40% and at least 33% in each subject to pass . Assume 3 subjects and take marks as an input from the user.

s1 = int(input("Enter the marks of subject 1\n"))
s2 = int(input("Enter the marks of subject 2\n"))
s3 = int(input("Enter the marks of subject 3\n"))

if s1<33 or s2<33 or s3<33:
    print("Your fail beacause your score less than 33 in one of the subject")
elif (s1+s2+s3)/3 < 40:
    print("Your fail beacuse your score less than 40%")
else:
    print("Congratulation!,Your pass")

    
