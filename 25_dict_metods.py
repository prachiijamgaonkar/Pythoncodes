mydict = {
    "key" : "value",
    "prach" : "morning",
    "list" :  [1,2,3],
    1:2,

    "prachi" : {"sani":54,#nested dictionaries we can us in the dictonaries
                
             "janu":65,
             "wedneday":47}
}
print(list(mydict.keys()))#prints the keys of dictionaries
print(list(mydict.values()))
print(list(mydict.items()))
print(mydict.keys())
print(mydict.values())
print(mydict.items())

updatedict  = {"shop" : "coffe",
               "Bio":"hey",
               "janu" :" 67"}
mydict.update(updatedict)#update the dictionary by addding key-values pairs from updatedict
print(mydict)


print(mydict.get("janu"))#print value associated with key"janu"
print(mydict["key"])#print value asssociated with "key"

#the diffrerence .get and [] syntax in dictionary
print(mydict.get("anshi"))#it returns none
print(mydict["anshi"])#it throws an that anshi is not in the dictionary