#Q Write a program to detect double space in a string

st = "This is a string with double spaces"

doubleSpaces = st.find("  ")

print(doubleSpaces)

st = st.replace(" ","  ")
print(st)
