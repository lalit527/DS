def maxHeapify(arr, n, index):
    left = 2* index
    right = 2* index + 1

    if left < n and arr[index] < arr[left]: 
        largest = left
    else:
        largest = index

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]

        maxHeapify(arr, n, largest)

def buildMaxHeap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        maxHeapify(arr, n, i)
    
    

def heapSort(arr): 
    buildMaxHeap(arr)
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        n = n - 1
        maxHeapify(arr, i, 0)

arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i])
