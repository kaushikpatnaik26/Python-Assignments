# 3. Recursive function to print n-digit strictly increasing numbers
def print_strictly_increasing_numbers(n, start=1, num=""):
    if n == 0:
        print(num)
        return
    for i in range(start, 10):
        print_strictly_increasing_numbers(n - 1, i + 1, num + str(i))
        
    
n = int(input('Enter num: '))
print_strictly_increasing_numbers(n)
