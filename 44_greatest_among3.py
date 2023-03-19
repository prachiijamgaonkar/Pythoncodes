#Write a program using function to find greatest of the numbers

def greatest(num1,num2,num3):
    
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

r=greatest(4,5,6)
print("Greatest number is "+" "+str(r))
