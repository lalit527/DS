class Result:
  def __init__(self):
    self.max = 0

def lis(arr):
  n = len(arr)
  r = Result()
  return _lis(arr, n, r)

def _lis(arr, n, r):
  if n == 1:
    return 1
  maxHere = 0
  for i in range(n):
    result = _lis(arr, i, r)
    if arr[i-1] < arr[n-1] and result + 1 > maxHere:
      maxHere = result + 1
  r.max = max(r.max, maxHere)
  return maxHere

def lis_memo(arr):
  n = len(arr)
  result = [1] * n

  for i in range(n):
    for j in range(0, i):
      print(i, j, end="---\n")
      if arr[i] > arr[j] and result[i] < result[j] + 1:
        result[i] = result[j] + 1
  maxHere = 0
  print(result)
  for i in range(n):
    if result[i] > maxHere:
      maxHere = result[i]

  return maxHere

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(lis_memo(arr))