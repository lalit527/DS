def cutRod(arr, size):
  if size <= 0:
    return 0
  _max = float('-inf')
  for i in range(size):
    _max = max(_max, arr[i] + cutRod(arr, size - i - 1))

  return _max

def cutRod_memoized(arr, size):
  result = [float('-inf')] * size
  return _cutRod_memoized(arr, size, result)

def _cutRod_memoized(arr, size, result):
  if result[size-1] >= 0:
    return result[size-1]
  if size == 0:
    q = 0
  else:
    q = float('-inf')
  
  for i in range(size):
    q = max(q, arr[i] + _cutRod_memoized(arr, size -i -1, result))

  result[size-1] = q
  return q

def cutRod_bottomup(arr, size):
  result = [0] * (size + 1)
  result[0] = 0
  for i in range(1, size + 1):
    q = float('-inf')
    for j in range(i):
      q = max(q, arr[j] + result[i - j - 1])
    result[i] = q
  return result[size]

arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
size = len(arr)
print("Maximum Obtainable Value is", cutRod_bottomup(arr, size))