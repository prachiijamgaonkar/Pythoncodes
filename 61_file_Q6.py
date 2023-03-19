#Write a program to mine a log file and find out whether it contains 'python'
with open ("log.txt") as f:
    content = f.read()

if 'python' in content.lower():#ye content ko lower case me kr deta hai,agr python upper case huaa to ye usko lower case me kr dega so..
    print("python is present")
else:
    print("No python is not present")