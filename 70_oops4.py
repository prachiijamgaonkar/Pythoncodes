class Employee:
    
    company = "youtube"
    salary = 100

    
obj1 = Employee()#always make object out of the class
obj2 = Employee()

#creating attributes of instance 
obj1.salary = 200
obj2.salary = 300

print(obj1.salary)#first it check the attritube which is along with obj is belong to object or not if its belong to object then only its takes attributes value from there
print(obj2.salary)#IF there is no such attribute belongs to object then it checked that attribute is belongs from class or not and if it is so that attribute value will be taking from class attribute


#print(obj2.address) throws an error as addreess is not present in instance/class