#Q6--> Can you change the self parameters inside a class to something elsee (say"prachi"). Try changing self to slf or prachi  and see the effect


class myclass:
    def __init__(prachi,name,roll_no):
        prachi.name = name
        prachi.roll_no = roll_no
    def details(prachi):
        print(f"Name : {prachi.name}")
        print(f"roll_no : {prachi.roll_no}")

my = myclass("sachi",78)
my.details()


#p so yes we can chnge the self parameeters inside a class 
