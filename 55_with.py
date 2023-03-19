with open('sample.txt','r') as f:#beacause of with statement ,don't need to use close function..as it is done automatically
   a= f.read()
   print(a)


with open("new.txt",'w')as c:
   v = c.write("prachi")
   print(v)

