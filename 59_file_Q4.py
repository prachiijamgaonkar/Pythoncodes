# A file contains a word "donkey" multiple times. You need to write a program which replaces this word with ####### by updating the same file 
with open ("sample.txt") as f:
    content = f.read()

content = content.replace("donkey","kuki")

with open("sample.txt",'w') as f:
    f.write(content)