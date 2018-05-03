def replace(arr):
    n = len(arr)
    b = [None] * n
    b[n-1] = -1
    for i in range(n-2, -1, -1):
        b[i] = max(b[i+1], arr[i+1])
    return b


arr = [16, 17, 4, 3, 5, 2]
print(replace(arr))