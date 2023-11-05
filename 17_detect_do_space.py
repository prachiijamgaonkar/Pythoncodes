#Q Write a program to detect double space in a string

st = "This is a string with double spaces"

doubleSpaces = st.find("  ")#when their is no double space in sentence it return (-1)

print(doubleSpaces)

st = st.replace(" ","  ")
print(st)
