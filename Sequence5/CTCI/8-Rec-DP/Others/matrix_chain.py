def matrix_order(dims):
  n = len(dims)
  T = [[0 for _ in range(n)] for _ in range(n)]
  for gap in range(2, n):
    for i in range(n - gap):
      j = i + gap
      T[i][j] = float('inf')
      for k in range(i + 1, j):
        temp = T[i][k] + T[k][j] + dims[i] * dims[k] * dims[j]
        if temp < T[i][j]:
          T[i][j] = temp
  return T[0][-1]