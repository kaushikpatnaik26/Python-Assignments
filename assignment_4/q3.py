def diplsay_menu():
    print("1, to create a list ")
    print("2, to display the list ")
    print("3, to insert in list ")
    print("4, to delete in list ")
    print("5, exit ")

def Createlist():
    global my_list
    my_list = []
    n = int(input("Enter number of elements to be in the list: "))
    my_list = [int(input("Enter element  :")) for _ in range(n)]

def display_list():
    print("The created list : ", my_list)
    
def insertlist():
    n = int(input("Enter an index to insert: "))
    m = int(input("Enter an element to be insert: "))
    my_list.insert(n,m)

def delList():
    n = int(input("Enter an index to del: "))
    del my_list[n]
my_list=[]

while True:

    diplsay_menu()
    choice = int(input("Enter a choice: "))
    if choice == 1:
        Createlist()
    elif choice == 2:
        display_list()
    elif choice == 3:
        insertlist()
    elif choice == 4:
        delList()
    elif choice == 5:
        print("thank youuuu <3")    
        break
    else:
        print("chala ja bsdk")


    
    
    

