if __name__ == '__main__':
    N = int(input())
    mylist=[]
    for i in range(N):
        fun = input().split()
        if fun[0]=="insert":
            mylist.insert(int(fun[1]),int(fun[2]))
        if fun[0]=="print":
            print(mylist)
        if fun[0]=="remove":
            mylist.remove(int(fun[1]))
        if fun[0]=="append":
            mylist.append(int(fun[1]))
        if fun[0]=="sort":
            mylist.sort()
        if fun[0]=="pop":
            mylist.pop()
        if fun[0]=="reverse":
            mylist.reverse()
            
#other method 

my_list = []

while True:
    print("\nCommands:\n1. append <value>\n2. insert <index> <value>\n3. remove <value>\n4. print\n5. sort\n6. reverse\n7. exit")
    command = input("Enter a command: ").split()
    if command[0] == "append":
        my_list.append(int(command[1]))
    elif command[0] == "insert":
        my_list.insert(int(command[1]), int(command[2]))
    elif command[0] == "remove":
        my_list.remove(int(command[1]))
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "reverse":
        my_list.reverse()
    elif command[0] == "exit":
        break
    else:
        print("Invalid command")
