#Q1 -->Create a class programmer for storing information of few programmers working at microsoft

class programmer:
    company = "Microsoft"

    def __init__(self):#when we have to take input from the user no need to take parameter in the pranthesis
            self.name = input("Enter the name of the programmer:\n")
            self.product = input("Enter the product of programmer:\n")

    def getinfo(self):
           print(f"Name of programmer :{self.name}")
           print(f"Product of progrrammer is: {self.product}")

obj1 =  programmer()

obj1.getinfo()







   

