
def josephus_recursive(n, k):
    if n == 1:  
        return 0
    return (josephus_recursive(n - 1, k) + k) % n  

def josephus_iterative(n, k):
    result = 0  
    for i in range(2, n + 1):  
        result = (result + k) % i  
    return result

if __name__ == "__main__":
    n, k = 7, 3  # Example case
    print("Recursive Josephus (n=7, k=3):", josephus_recursive(n, k))
    print("Iterative Josephus (n=7, k=3):", josephus_iterative(n, k))
