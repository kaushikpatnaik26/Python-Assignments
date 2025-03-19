# import random

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] >= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# def quickselect(arr, low, high, k):
#     if low == high:
#         return arr[low]
    
#     pivot_index = random.randint(low, high)
#     arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
#     partition_index = partition(arr, low, high)
    
#     if partition_index == k:
#         return arr[partition_index]
#     elif partition_index < k:
#         return quickselect(arr, partition_index + 1, high, k)
#     else:
#         return quickselect(arr, low, partition_index - 1, k)

# def find_kth_largest(arr, k):
#     return quickselect(arr, 0, len(arr) - 1, k - 1)

# arr = [12, 3, 5, 7, 19, 1, 8, 17]
# k = int(input("enter value of k : "))
# print(f"The {k}th largest element is: {find_kth_largest(arr, k)}")

import random

def quickselect(arr, k):
    if not arr:  
        return None

    pivot = random.choice(arr)

    left = [x for x in arr if x > pivot]  
    right = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]  

    if k <= len(left):  
        return quickselect(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else: 
        return quickselect(right, k - len(left) - len(equal))  

arr = [12, 3, 5, 7, 19, 1, 8, 17]
k = int(input("enter value of k : "))
print(f"The {k}th largest element is: {quickselect(arr, k)}")
