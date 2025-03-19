import time

def fast_power(a, b):
    if b == 0:  
        return 1
    elif b % 2 == 0: 
        half_power = fast_power(a, b // 2)
        return half_power * half_power
    else:  
        return a * fast_power(a, b - 1)


a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

start = time.time()
result = fast_power(a, b)
end = time.time()


print(f"Recursive Approach: {a}^{b} = {result}")
print("Recursive Execution Time:", end - start)

