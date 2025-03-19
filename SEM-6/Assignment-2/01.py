# 1. Recursive power function
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(f'{power(5, 3)}')