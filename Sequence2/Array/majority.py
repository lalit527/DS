def getMajority(arr):
    n = len(arr)
    majority_ele = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] == majority_ele:
            count += 1
        elif arr[i] != majority_ele:
            count -= 1
        
        if count == 0:
            majority_ele = arr[i]
            count = 1
    if isMajority(arr, n, majority_ele):
        return majority_ele
    
    return -9999

def isMajority(arr, n, ele):
    count = 0
    for i in arr:
        if i == ele:
            count += 1

    if count > (n // 2):
        return True
    
    return False
    
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(getMajority(arr))