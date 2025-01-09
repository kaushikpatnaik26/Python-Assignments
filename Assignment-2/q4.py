list = [1,2,3,4,5,4,4,4,4,6,6]
n = int(input("enter a element to be removed from the lsit: "))
while n in list:
    list.remove(n)
print("the updated list is :  ", list)
