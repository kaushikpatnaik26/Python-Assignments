
def recursive_sum(n):
    if n == 1:  # Base case
        return 1
    return n + recursive_sum(n - 1)  


def iterative_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def formula_sum(n):
    return (n * (n + 1)) // 2


if __name__ == "__main__":
    n = 10  # Test case
    print("Recursive Sum (n=10):", recursive_sum(n))
    print("Iterative Sum (n=10):", iterative_sum(n))
    print("Formula Sum (n=10):", formula_sum(n))
