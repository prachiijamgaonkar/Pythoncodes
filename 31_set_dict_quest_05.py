'''create a empty dictionariey . Allow 4 friends  to enter their favourite languagee as 
values and use keys as thier names. Determine that the namees are unique'''

dict = {}

a = input("Enter your  lang Harsh:\n")
b = input("Enter You lang yash:\n")
c = input("Enter your sani:\n")
d = input("Enter your  prachi:\n")

dict["Harsh"] = a
dict["Yash"] = b
dict["sani"] = c#values are changeble ...but keys are must be unique
dict["prachi"] = d

print(dict)

#if here two frds name are same it will  print updated pair not a old one....beacuz we want unique keys in dict



