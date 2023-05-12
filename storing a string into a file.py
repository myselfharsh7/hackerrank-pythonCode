#creating a file to store  a string :
# open the file to store a string 
f= open("myfile.txt","w")

#enter the string from the keyboard
print('enter text (@ at the end)')

while str !='@':
    str = input()
    if str!='@':
        f.write(str + '\n')
f.close()
