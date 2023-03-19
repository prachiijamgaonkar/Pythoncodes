a = {1,2,3,4,5,1}
print(type(a))
print(a)

#important :This syntax will create an empty dictionary and not a emty set
a={}
print(type(a))

#empty set can be created using below set
b = set()
print(type(b))

#methods of set
b={1,2,3,4,5}
b.add(5)
b.add(5)#adding a value repeatedly does not chnges a set
b.add(4)

#b.add([1,2,3])#list are mutable  so for that wee can't addd it in set
b.add((7,8,9))#tuple we can add in set
#-b.add({3:5})#dictionary also we cant add in set
print(b)

print(len(b))
b.remove(5)
#b.remove(15)#throws an error becoz its not in set

print(b)

print(b.pop())#it retun any one elment from set....koi bhi ek number in random way