def missingOne(arr):
    n = len(arr) + 1
    tmp1 = 0
    tmp2 = 0
    for i in range(n-1):
        tmp1 = tmp1 ^ arr[i]
    for i in range(1, n+1, 1):
        tmp2 = tmp2 ^ i
    return tmp1 ^ tmp2
arr = [2, 5, 3, 4, 1, 7]
print(missingOne(arr))