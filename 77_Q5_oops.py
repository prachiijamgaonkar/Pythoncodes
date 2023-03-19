#Q5 Write a class Train which which has methods to book a ticket,get stataus(no of seats) and get fare information of  trains running under indian railway
class Train:
    def __init__(self):
        self.name = input("Enter name of the train:\n")
        self.fare = int(input("Enter fare:\n "))
        self.seats = int(input("Enter seats:\n"))

    def getstatus(self):
        print("\nTRAIN  & SEATS")
        print("********************")
        print(f"Name : {self.name}")
        print(f"NO of seats available : {self.seats}")

    def getfare(self):
        print(f"The price of the  ticket is : {self.fare}")

    def bookedticket(self):
        if(self.seats > 0):
            print(f"Your ticket has been booked,your ticket number is {self.seats}")
            self.seats = self.seats-1
        else:
            print(f"Seats are full kindly apply through tatkal\n")


tra1 = Train()

tra1.getstatus()
tra1.getfare()
tra1.bookedticket()

tra1.getstatus()



