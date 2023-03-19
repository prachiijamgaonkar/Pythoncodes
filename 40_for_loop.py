fruits = ["banana","jamun","graphs","chiku"]

for item in fruits:
    print(item)       

#range
for i in range(0,9,2):#(start,stop,step_size)
    print(i)  

for i in range(0,9):
    print(i)

for i in range(6):
    print(i) 

#for with else
for i in range (0,6):
    print("*"*i)
else:#it execute when your or loop succesfully execute
    print("congrats!Your placed")    


#break statement
for i in range(10):
    print(i)
    if(i==5):
        break#if for loop is execute due to break then else part is not get executed
else:
    print("something")


#continue statement
for i in range(18):
    if(i==5):#continue skip the value that u set equal to the variable i,here it skip 5 and then continue after that
        continue
    print(i)



#for even numbers
for i in range(0,9):
    if(i%2 != 0):
        continue
    print(i)



#for pass statements
i=5

if i<3:
    pass #do nothing,its a null statement
print("prachi HI!!")



