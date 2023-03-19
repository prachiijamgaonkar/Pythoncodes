#Q4-> Create a class with a class attribute a; create an object from it and set a directly using object a = 0. Does this chnge the class attributes?

class sample:
    a = "prachi"

obj = sample()
obj.a = 0

print(sample.a)
print(obj.a)

#it dosent chnge the class attributes not at all...it create new attribute of object
