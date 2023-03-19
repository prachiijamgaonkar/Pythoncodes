#Write  a program which find whether a given name is present in a list or not.
names = ["harry","shipra","sachi","janvi","addithi"]

name = input("Enter the name to check:\n")


if name in names:
    print("Your name is present im the list")
else:
    print("Your name is not present in the list")