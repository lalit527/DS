def optimalStrategy(arr, n):
  table = [[0 for i in range(n)] for j in range(n)]
  for gap in range(n):
    i = 0
    for j in range(gap, n):
      x = table[i + 2][j] if (i + 2) <= j else 0
      y = table[i + 1][j - 1] if (i + 1) <= (j-1) else 0
      z = table[i][j - 2]  if i <= (j-2) else 0

      table[i][j] = max(arr[i] + min(x, y),
                      arr[j] + min(y, z))
      i += 1

  return table[0][n - 1]

arr = [8, 15, 3, 7]
n = len(arr)
print(optimalStrategy(arr, n))