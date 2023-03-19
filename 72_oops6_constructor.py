class student:
    def __init__(self,name,roll_no,section,department):
    
        print(f"Roll no {roll_no} details are as follows:\n")
        self.name = name
        self.roll_no = roll_no
        self.section = section
        self.department = department

    def mydetails(self):
        print(f"Name : {self.name}")
        print(f"Section : {self.roll_no}")
        print(f"Department :{self.department}")

obj1 = student("prachi",34,"c","ETC")#we have give the valuues of constructor like that while creating object in class function
#obj1 = student() ->throws an error that missing 4 positional arguments
obj1.mydetails()