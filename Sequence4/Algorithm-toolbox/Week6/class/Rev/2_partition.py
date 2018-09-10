def partition(A, n):
  sums = 0
  for i in A:
    sums += i

  if sums % 3 != 0:
    return 0

  cols = n + 1
  rows = sums // 3 + 1

  T = [[0 for j in range(cols)] for i in range(rows)]

  for j in range(cols):
    T[0][j] = 1

  for j in range(1, rows):
    T[i][0] = 0

  for i in range(1, rows):
    for j in range(1, cols):
      T[i][j] = T[i][j -1]
      if i >= A[j - 1]:
        T[i][j] = T[i][j] or T[i - A[j - 1]][j - 1]
  print(T)
  return T[rows -1][cols - 1]

n = 11
A = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
partition(A, n)