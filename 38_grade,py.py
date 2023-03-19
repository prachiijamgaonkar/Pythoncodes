marks = int(input("Enter a marks"))

if marks > 100 or marks < 0:
    print("Invalid Input")
    
elif marks >90 and marks <100 :
    grade = "Ex"

elif marks > 80 and marks < 90 :
    grade = "A"

elif marks > 70 and marks < 80:
    grade = "B"

elif marks > 60 and marks < 70:
    grade ="c"

elif marks > 50 and marks < 60:
    grade ="D"

print("Your Grade:"+grade)