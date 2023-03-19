#Q11 Write a program to remove a file to "renamed_by_python.txt"
import os
oldname = "sample2.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
   content= f.read()

with open(newname,"w") as f:
    f.write(content)

os.rename(oldname)


