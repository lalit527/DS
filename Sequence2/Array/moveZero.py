def replaceZero(arr):
    n = len(arr)
    i = 1
    j = 0
    while i < n and j < n:
        if arr[j] != 0:
            j += 1
        elif arr[i] == 0:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
            j += 1
    return arr

arr = [0, 1, 0, 2, 0, 0, 3, 4, 5, 0]
print(replaceZero(arr))