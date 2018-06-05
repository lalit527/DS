def peak_finder(arr):
  n = len(arr)
  max_index = 0
  for i in range(n):
    if i == 0 and arr[i] > arr[i + 1]:
      print(arr[i])
    elif (i == n - 1) and arr[i] > arr[i - 1]:
      print(arr[i])
    elif arr[i - 1] <= arr[i] >= arr[i + 1]:
      print(arr[i])

def peak_finder_better(arr):
  n = len(arr)
  index = _peak_finder_better(arr, 0, n - 1)
  return arr[index]

def _peak_finder_better(arr, start, end):
  if start > end:
    return -99
  
  mid = start + (end - start) // 2
  if ((((mid == 0) or arr[mid - 1]) <= arr[mid] and
      ((mid == n - 1) or arr[mid + 1] <= arr[mid]))):
    return mid
  
  elif (mid > 0 and arr[mid - 1] > arr[mid]):
    return _peak_finder_better(arr, start, (mid - 1))
  
  else:
    return _peak_finder_better(arr, (mid + 1), end)


arr = [1, 3, 0, 4, 1, 7]
n = len(arr)
print(peak_finder_better(arr))