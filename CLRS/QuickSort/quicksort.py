def _quicksort(arr, s, e):
  if s < e:
    q = partition(arr, s, e)
    _quicksort(arr, s, q-1)
    _quicksort(arr, q+1, e)

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