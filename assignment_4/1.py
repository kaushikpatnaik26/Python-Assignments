# Write a program that reads three integers from the user and displays them in sorted order (from
# smallest to largest). Use the min and max functions to find the smallest and largest values. The middle
# value can be found by computing the sum of all three values, and then subtracting the minimum value
# and the maximum value.

n,m,z = 10,31,20

print(min(n,m,z))
print(max(n,m,z))
print("sum = " ,(n+m+z))
print("diff = " ,(n-m-z))