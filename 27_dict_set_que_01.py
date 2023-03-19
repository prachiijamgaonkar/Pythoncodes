#Q1 write a program to create a dictionaries of hindi word with the values as their english translation .Provide user with an option to look it up!
mydict ={"pankha": "Fan0",
         "DABBa": "box",
         "chai" : "tea"}
print("Options are",mydict.keys())

a = input("Enter the hindi word\n")
#print("The meaning of your word is",mydict[a])//it returns error

print("The meaning of your word is",mydict.get(a))#so for that we us it and not crash our programm