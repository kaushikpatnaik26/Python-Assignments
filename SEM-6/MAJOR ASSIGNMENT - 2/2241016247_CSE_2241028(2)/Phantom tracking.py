
def extract_suspicious(transactions, threshold):
    return [t for t in transactions if t > threshold]


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


transactions = [120, 45, 300, 220, 90, 600, 130, 75, 800, 500, 350, 40]
threshold = 250
search_amount = int(input("Enter an amount to search for: "))


suspicious_transactions = extract_suspicious(transactions, threshold)
sorted_suspicious = selection_sort(suspicious_transactions)
found = binary_search(sorted_suspicious, search_amount)
sorted_transactions = merge_sort(transactions)


if __name__ == "__main__":
    print("Suspicious Transactions:", suspicious_transactions)
    print("Sorted Suspicious Transactions:", sorted_suspicious)
    print(f"Is {search_amount} in Suspicious Transactions?", found)
    print("Sorted Full Transactions:", sorted_transactions)
