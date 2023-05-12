# creating a file to store a character :
f = open("myfile.txt","w")

#enter character from keyboard
str = input("enter text to store : ")

#write the string into the file
f.write(str)

#closing the file
f.close()


