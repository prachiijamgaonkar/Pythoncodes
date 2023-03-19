#Q Write a program to find out whethear a file is identical and makes the content of another file 

file1 = "this.txt"
file2 = "copy.txt"

with open ("this.txt") as f:
    file1 = f.read()

with open ("copy.txt") as f:
    file2 = f.read()

if file1 == file2:
    print("File is idenical")
else:
    print("File is not identical")

