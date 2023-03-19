mydict = {
    "key" : "value",
    "prach" : "morning",
    "list" :  [1,2,3],

    "prachi" : {"sani":54,#nested dictionaries we can us in the dictonaries
                
             "janu":65,
             "wedneday":47}
}
print(mydict['prachi']['janu'])
print(mydict['prach'])
print(mydict['key'])
mydict['key'] = [45,23]#dictionaries are mutable
print(mydict)
