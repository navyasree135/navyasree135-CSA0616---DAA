arr = [64, 25, 12, 22, 11]

n = len(arr)
for i in range(n):
    # Find the minimum element in the unsorted part
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    # Swap the found minimum element with the first element
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Sorted:", arr)
