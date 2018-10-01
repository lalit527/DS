def matrix_chain(arr):
  n = len(arr)
  return _matrix_chain(arr, 1, n - 1)

def _matrix_chain(arr, i, j):
  if i == j:
    return 0
  min_value = float('inf')
  for k in range(i, j):
    count = _matrix_chain(arr, i, k) + _matrix_chain(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
    if count < min_value:
      min_value = count
  return min_value

def matrix_chain_dp(arr):
  n = len(arr)
  T = [[0 for _ in range(n)] for _ in range(n)]
  for l in range(2, n):
    for i in range(n - l):
      j = i + l
      T[i][j] = float('inf')
      for k in range(i + 1, j):
        temp = T[i][k] + T[k][j] + arr[i] * arr[k] * arr[j]
        if temp < T[i][j]:
          T[i][j] = temp
  return T



arr = [1, 2, 3, 4, 3]; 
print(matrix_chain_dp(arr))