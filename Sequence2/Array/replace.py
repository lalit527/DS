def replace(arr):
    n = len(arr)
    b = [None] * n
    b[n-1] = -1
    for i in range(n-2, -1, -1):
        b[i] = max(b[i+1], arr[i+1])
    return b

def replaceInPlace(arr):
    n = len(arr)
    maxEle = -1
    for i in range(n-1, -1, -1):
        tmp = arr[i]
        arr[i] = maxEle
        maxEle = max(maxEle, tmp)
    return arr


arr = [16, 17, 4, 3, 5, 2]
print(replaceInPlace(arr))