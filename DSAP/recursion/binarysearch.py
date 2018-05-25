def binarySearch(arr, target, low, high):
  if low > high:
    return False
  mid = (low + high) // 2
  if arr[mid] == target:
    return True
  elif arr[mid] < target:
    return binarySearch(arr, target, mid + 1, high)
  else:
    return binarySearch(arr, target, low, mid - 1)

arr = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
print(binarySearch(arr, 37, 0, len(arr) - 1))