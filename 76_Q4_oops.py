#Q4-> ADD Static method in problem2 to greet the user with hello

class calculator:
    def __init__(self):
        self.n = int(input("Enter the number :\n"))
    
    def mysquare(self):
        print(f"Square of {self.n} is {self.n**2}")

    def mycube(self):
        print(f"Cube of {self.n} is {self.n**3}")

    def mysquaroot(self):
        print(f"Squar00t of {self.n} is {self.n**0.54}")
    
    @staticmethod
    def mygreet():
        print("-- Hello --")


cal = calculator()
cal.mysquare()
cal.mycube()
cal.mysquaroot()
cal.mygreet()


                
