def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted
    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort

# Example usage
nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = quick_sort(nums)
print("Sorted array:", sorted_nums)
