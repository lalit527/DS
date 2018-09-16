def magic_index_fast(arr):
  if arr is None:
    return -1
  return _magic_index_fast(arr, 0, len(arr) - 1)


def  _magic_index_fast(arr, s, e):
  if e < s:
    return -1

  mid = (s + e) // 2
  mid_value = arr[mid]
  if mid_value == mid:
    return mid

  # Search left first
  left_index = min(mid - 1, mid_value)
  left =  _magic_index_fast(arr, s, left_index)
  if left >= 0:
    return left
  
  # search right
  right_index = max(mid + 1, mid_value)
  right = _magic_index_fast(arr, right_index, e)

  return right


if __name__ == "__main__":
  A = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
  print(magic_index_fast(A))