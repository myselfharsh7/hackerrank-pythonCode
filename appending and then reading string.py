# appending and then reading string 
# open the file for reading data

f=open ("myfile.txt","a+")

# enter data from keyborad
print ("enter the data to append: ") 

while str !='@':
    str = input()  #accept string to str
    if str != '@':
        f.write(str + '\n')
# put the file pointer to the beginning of the file
f.seek(0,0)

# read string from file
print("the content of the file are : ")
str = f.read()
print(str)

# closing the file
f.close()
