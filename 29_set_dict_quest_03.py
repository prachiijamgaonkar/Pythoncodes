#Q3  Can we have a set with 18(int ) and "18"(str) as a values in it?

s ={ 18,"18"}
print(s)

s={18,"18",4.1}
print(s)

d=set()
d.add(20)
d.add(20.0)
d.add("21")
print(d)
print(len(d))#it would be 2
