#3=>  A Spam comment is defined as an a text containing following keywords:
#"make a lot of money","buy now","subscribe this","click this".Write a program to detect these spams

text = input("Enter the text:\n")
if("make a lot of money" in text):
    spam = True
elif("buy"in text):
    spam = True
elif("click this" in text):
    spam = True
elif("Subscribe this" in text):
    spam = True
else:
    spam =False

if(spam):
    print("This text is spam")
else:
    print("This test is not set to spam")