#Write a program to read the text from a given file "poems.txt" and find out whether it contains word "Twinkle"

with open("poems.txt") as f:#it take bydefault read mode
    d = f.read()

if 'Twinkle' in d:
    print("Twinkle is present in file")
else:
    print("Twinkle is not present in file")

#another way 
f=open("poems.txt",'r')
c= f.read()
if 'Twinkle' in c:
    print("Twinkle is present in file")
else:
    print("Twinkle is not present in file")
f.close()
