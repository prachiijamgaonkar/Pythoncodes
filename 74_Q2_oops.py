#Q2-->Write a class calulator capable of finding square , cube and squareroot of a number.

class calculator:
    def __init__(self):
        self.n = int(input("Enter the number :\n"))
    
    def mysquare(self):
        print(f"Square of {self.n} is {self.n**2}")

    def mycube(self):
        print(f"Cube of {self.n} is {self.n**3}")

    def mysquaroot(self):
        print(f"Squar00t of {self.n} is {self.n**0.54}")





cal = calculator()
cal.mysquare()
cal.mycube()
cal.mysquaroot()


                
