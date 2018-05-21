def _minJump(arr, s, e):
  if s == e:
    return 0
  if arr[s] == 0:
    return float('inf')

  min = float('inf')

  for i in range(s+1, e+1):
    if i < s + arr[s] + 1:
      jumps = _minJump(arr, i, e)
      if jumps != float('inf') and jumps + 1 < min:
        min = jumps + 1
  return min

def minJump(arr):
  n = len(arr)
  return _minJump(arr, 0, n-1)

def minJump_memo(arr):
  n = len(arr)
  return _minJump_memo(arr, n)

def _minJump_memo(arr, n):
  jumps = [0 for i in range(n)]
  if n == 0 or arr[0] == 0:
    return float('inf')
  jumps[0] = 0
  for i in range(1, n):
    jumps[i] = float('inf')
    for j in range(i):
      if ((i <= j + arr[j]) and (jumps[j] != float('inf'))):
        jumps[i] = min(jumps[i], jumps[j] + 1)
        break
  print(jumps)
  return jumps[n-1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJump_memo(arr))