#Use open function to read the content of a file
#if we do not take a mode here,so it take bydefault a 'r' mode
f = open("sample.txt",'r')#open the file in readd mode
data = f.read()#read its vontent
#It can read a first 5 character of a file (data = f.read(5))
print(data)#print its content
f.close()#close the file