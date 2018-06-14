#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    l = len(a) + 1
    m = len(b) + 1
    n = len(c) + 1
    T = [[[0 for i in range(n)] for j in range(m)] for k in range(l)]
    for i in range(1, l):
      for j in range(1, m):
        for k in range(1, n):
          if a[i - 1] == b[j - 1] and a[i-1] == c[k - 1]:
            T[i][j][k] = 1 + T[i-1][j-1][k-1]
          else:
            T[i][j][k] = max(T[i-1][j][k], T[i][j-1][k], T[i][j][k-1],
                             T[i-1][j-1][k], T[i-1][j][k-1], T[i][j-1][k-1])
    return T[l-1][m-1][n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
