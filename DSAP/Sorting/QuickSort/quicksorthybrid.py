def insertionSort(arr, s, e):
  for j in range(s+1, e+1):
    key = arr[j]
    i = j - 1
    while i >= s and arr[i] > key:
      arr[i + 1] = arr[i]
      i = i - 1
    arr[i + 1] = key

def _quicksort(arr, s, e):
  if (e - s) > 2:
    q = partition(arr, s, e)
    _quicksort(arr, s, q-1)
    _quicksort(arr, q+1, e)
  else:
    insertionSort(arr, s, e)

def partition(arr, s, e):
  x = arr[e]
  i = s - 1
  for j in range(s, e):
    if arr[j] <= x:
      i = i + 1
      arr[j], arr[i] = arr[i], arr[j]
  arr[i + 1], arr[e] = arr[e], arr[i+1]
  return i + 1


def quicksort(arr):
  n = len(arr)
  _quicksort(arr, 0, n-1)

arr = [ 12, 11, 13, 5, 6, 7]
quicksort(arr)
print(arr)