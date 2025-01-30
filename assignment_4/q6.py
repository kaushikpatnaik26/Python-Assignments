''' Input 10 integers from the keyboard into a list. The number to be searched is entered through the
keyboard by the user. Write a Python program to find if the number to be searched is present in the
list and if it is present, display the number of times it appears in the list.'''

my_list = [int(input("Enter elements to the list: ")) for _ in range (5)]
search = int(input("Enter the number to be searched: "))
count = my_list.count(search)

if (count > 0):
    print(f"the number is in the list n appears {count} times ")
else: 
    print("the number is not in list")
