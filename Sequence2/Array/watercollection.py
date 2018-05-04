def waterCollected(arr):
    n = len(arr)
    left = [None] * n
    right = [None] * n
    max = -99
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
        left[i] = max

    max = -99
    for i in range(n-1, -1, -1):
        if arr[i] > max:
            max = arr[i]
        right[i] = max
    sum = 0
    for i in range(n):
        sum += min(left[i], right[i]) - arr[i]

    return sum

def waterCollected2(arr):
    n = len(arr)
    left = [None] * n
    max = -99
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
        left[i] = max

    max = -99
    sum = 0
    for i in range(n-1, -1, -1):
        if arr[i] > max:
            max = arr[i]
        sum += min(left[i], max) - arr[i]
    
    return sum

arr = [1, 3, 6, 2, 0, 7]
print(waterCollected2(arr))