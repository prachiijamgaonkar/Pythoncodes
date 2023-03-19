class myclass:
    salary = "70000k"
    company = "zomato"

    def getsalary(self):
        print(f"Hlw {self.name},Your selected in cognizant at a salary of {self.salary} per month")

    @staticmethod#beacause of method we dont have a need to take self as a parameter in our method
    def greet():
        print("Good morning ,dear")

    @staticmethod#hm kitnee bhi static method bna sk skte hai
    
    def time():
        print("time is 9am in the morning")

    


harry = myclass()
harry.name = "prachi"
harry.getsalary()# is equal to myclass.salary(harry)
harry.greet()# is equal to myclass.greet()




