def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i>=0 and arr[i] >  key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key

a = [9, 4, 2, 5, 7, 6, 8, 3]
#print(a)
insertionSort(a)
print(a)