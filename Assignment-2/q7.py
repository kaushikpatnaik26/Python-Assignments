def cumulative_list(numbers):
    cumulative = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        cumulative.append(current_sum)
    return cumulative

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

result = cumulative_list(numbers)

print("The cumulative list is:", result)
