#Repeat program of Q4 for a list of such words to be sensored

words = ["donkey","harry","chara"]
with open ("sample.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"$%@$^#")

with open("sample.txt",'w') as f:
    f.write(content)
