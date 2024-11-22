def find_kth_missing(arr,k):
    for i in range(1, arr[-1]+k+1):
        if i not in arr:
            k-=1
            if k==0:
                return i
arr = [2, 3, 4, 7, 11]
k=5
print(find_kth_missing(arr, k))  

