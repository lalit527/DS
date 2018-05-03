def zigZag(arr):
    small = True
    n = len(arr)
    i = 1
    while i < n:
        if small and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
        elif not small and arr[i-1] < arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
        i += 1
        small = not small
    return arr
        
        
arr = [4, 3, 7, 8, 6, 2, 1]
out = [3, 7, 4, 8, 2, 6, 1]
print(zigZag(arr))