def quickSort(arr, first, last):
    if first <  last:
        partition = getPartition(arr, first, last)
        quickSort(arr, first, partition-1)
        quickSort(arr, partition+1, last)

def getPartition(arr, first, last):
    lastEle = arr[last]
    i = first-1
    for j in range(first, last, 1):
        if arr[j] <= lastEle:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[last] = arr[last], arr[i+1]
    return i+1

arr = [ 12, 11, 13, 5, 6, 7]

n = len(arr)
quickSort(arr, 0, n-1)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i])