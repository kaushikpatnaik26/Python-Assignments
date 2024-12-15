from math import pi

def circlearea(r):
    print("area of the circle is : ", (pi*r**2))

def volume(r):
    print("volume of the circlce is :" , (4/3 * pi * r**3))

r = float(input("enter a radius : "))
circlearea(r)
volume(r)