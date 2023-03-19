#Write a program to generate multiplication tables from 2 to 20 and write it to the different files .Place these files in a folder for a 13 yr old

for i in range (2,21):

    with open (f"tables/Multiplication_table_of_{i}",'w') as f:#for putting folder and file at a time so we have to put forward slash(/)between the name of folder and file
     for j in range(1,11):
            f.write(f"{i}X{j} = {i*j}")
            if(j != 10):
                f.write('\n')
                
            
