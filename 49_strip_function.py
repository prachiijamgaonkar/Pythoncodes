#Write a python program to remove a word from string and strip it at the same time

def remove_and_strip(string,word):
    new = string.replace(word," ")#replace word eith space
    return new.strip()#remove the space at end and fromt of string

this = "Hlw, Homies!"
print(remove_and_strip(this,"Hlw"))


def remove_and_split(string,word):
    new = string.replace(word," ")#replace word eith space
    return new.split()#distributr string into list

this = "Hlw,my Homies!"
print(remove_and_split(this,"Hlw"))

