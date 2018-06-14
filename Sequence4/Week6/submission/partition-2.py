# Uses python3
import sys

def partition2(A, n):
  sums = 0
  for i in A:
    sums += i

  if sums % 3 != 0:
    return 0
  
  cols = n + 1
  rows = sums // 3 + 1

  T = [[0 for i in range(cols)] for j in range(rows)]

  for i in range(cols):
    T[0][i] = 1

  for i in range(1, rows):
    T[i][0] = 0

  for i in range(1, rows):
    for j in range(1, cols):
      T[i][j] = T[i][j - 1]
      if i >= A[j - 1]:
        T[i][j] = T[i][j] or T[i - A[j-1]][j - 1]

  return T[rows - 1][cols - 1]





if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition2(A, n))