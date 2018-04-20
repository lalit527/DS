def arrayPairSum(arr, sum):
    makeSum = {}
    for i in range(len(arr)):
        makeSum[sum - arr[i]] = i

    for i in arr:
       if i in makeSum:
           return True
    return False


    
        

arr = [1, 2, 2, 3]
sum = 4
print(arrayPairSum(arr, sum))