def rotate(a,b,c):
    return c,a,b
tup = "dough" , 22, 1987
a,b,c = tup
for x in range (3):
    a,b,c = rotate(a,b,c)
    print(a,b,c)
