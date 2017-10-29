def bubbleSort(arr):
    count = 0
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-1-i):
            count += 1
            if arr[j] > arr[j+1]:
                swapped = True
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
        if swapped == False:
            break
    print(count)

def merge(arr, first, last, mid):
    l = mid - first + 1
    r = last - mid
    #i, j, k = 0
    leftArray = [None] * l
    rightArray = [None] * r
    
    for i in range(0,l):
        leftArray[i] = arr[first+i]
    
    for i in range(0,r):
        rightArray[i] = arr[mid+1+i]
        
    i=0
    j=0
    k=first
    
    while i < l and j < r:
        if leftArray[i] < rightArray[j]:
            arr[k] = leftArray[i]
            i += 1
            k += 1
        else:
            arr[k] = rightArray[j]
            j +=1
            k +=1
    
    while i < l:
        arr[k] = leftArray[i]
        i += 1
        k += 1
        
    while j < r:
        arr[k] = rightArray[j]
        j +=1
        k +=1
    
    
def _mergeSort(arr, first, last):
    if first < last:
        mid = (first+last)//2
        _mergeSort(arr, first, mid)
        _mergeSort(arr, mid+1, last)
        merge(arr, first, last, mid)
 
def mergeSort(arr):
    _mergeSort(arr, 0, len(arr)-1)
    

def partition(arr, first, last):
    pivot = first
    left  = first + 1
    right = last 
    part  = False
    while not part:
        while left <= right and arr[pivot] >= arr[left]:
            left += 1
        while right >= left and arr[pivot] <= arr[right]:
            right -= 1
        #print(left, right)
        if right < left:
            part = True
        else:
            tmp = arr[left]
            arr[left]  = arr[right]
            arr[right] = tmp
    tmp = arr[pivot]
    arr[pivot] = arr[right]
    arr[right] = tmp
    
    return right
    
    
def _quickSort(arr, first, last):
    if first <  last:
        part = partition(arr, first, last)
        #print(part)
        _quickSort(arr, first, part-1)
        _quickSort(arr, part+1, last)
        
def quickSort(arr):
    _quickSort(arr, 0, len(arr)-1)

    
    
a = [9, 4, 2, 5, 7, 6, 8, 3]
print(a)
quickSort(a)
print(a)