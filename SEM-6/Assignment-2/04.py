def nth_fibonacci(n):
    if n <= 1:
        return n
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

print(f'{nth_fibonacci(1)}')

'''
    Time Complexity = O(2 ^ n)
'''