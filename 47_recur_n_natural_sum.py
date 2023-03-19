#WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST n NATURAL NUMBERS
#sum(n) = sum(n-1)+n
#n! = (n-1)!*n;

def rcur_sum(n):
    if n <=1:
        return n
    else:
        return n +rcur_sum(n-1)
    
print(rcur_sum(9))

#chnge this value for different reseaons
num=19

if num<0:
    print("Enter positive integer")
else:
    print("The sum of naturral number is"+" "+str(rcur_sum(num-1)*num))
