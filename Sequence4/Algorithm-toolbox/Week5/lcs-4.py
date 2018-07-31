#Uses python3

import sys

def lcs2(a, b):
  #write your code here
  m = len(a) + 1
  n = len(b) + 1
  print(a, b)
  T = [[0 for i in range(n)] for j in range(m)]
  print(T)
  for i in range(1, m):
    for j in range(1, n):
      if a[i - 1] == b[j - 1]:
        T[i][j] = 1 + T[i-1][j-1]
      else:
        print(i, j)
        T[i][j] = max(T[i-1][j], T[i][j-1])
  print(T)
  return T[m-1][n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
