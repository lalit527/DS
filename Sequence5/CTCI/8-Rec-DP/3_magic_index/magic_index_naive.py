def magic_index(arr):
  if arr is None:
    return -1
  
  for index, value in enumerate(arr):
    if index == value:
      return value


def magic_index_fast(arr):
  if arr is None:
    return -1
  return _magic_index_fast(arr, 0, len(arr) - 1)


def  _magic_index_fast(arr, s, e):
  if e < s:
    return -1
  mid = (s + e) // 2
  if arr[mid] == mid:
    return mid
  elif arr[mid] > mid:
    return _magic_index_fast(arr, s, mid - 1)
  else:
    return _magic_index_fast(arr, mid, e)


if __name__ == "__main__":
  A = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
  print(magic_index_fast(A))