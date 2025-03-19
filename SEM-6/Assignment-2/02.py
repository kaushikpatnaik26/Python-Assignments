# 2. Recursive GCD function
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
print(f'{gcd(10, 150)}')
