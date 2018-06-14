# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def isSubsetSum(A, n, sums):
  if sums == 0:
    return 1
  
  if n == 0 and sums != 0:
    return 0

  if A[n - 1] > sums:
    return isSubsetSum(A, n - 1, sums)

  return isSubsetSum(A, n - 1, sums) or isSubsetSum(A, n - 1, sums - A[n-1])

def partition1(A, n):
  sums = 0
  for i in A[:n]:
    sums += i

  if sums % 3 != 0:
    return 0

  return isSubsetSum(A, n, sums // 3)

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

  for i in range(rows):
    T[i][0] = 0

  for i in range(rows):
    for j in range(cols):
      T[i][j] = T[i][j - 1]
      if i >= A[j - 1]:
        T[i][j] = T[i][j] or T[i - A[j-1]][j - 1]
  
  print(T)
  return T[rows - 1][cols - 1]





if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition2(A, n))

