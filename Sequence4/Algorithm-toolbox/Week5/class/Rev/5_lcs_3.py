import sys

def lcs3(a, b, c):
  n = len(a)
  m = len(b)
  l = len(c)
  if m == 0 or n == 0 or l == 0:
    return 0
  
  if a[n-1] == b[m-1] == c[l - 1]:
    return 1 + lcs3(a[:n-1], b[:m-1], c[:l-1])

  return max(lcs3(a[:n-1], b[:m], c[:l]), 
             lcs3(a[:n], b[:m-1], c[:l]),
             lcs3(a[:n], b[:m], c[:l-1]),
             lcs3(a[:n-1], b[:m-1], c[:l]),
             lcs3(a[:n-1], b[:m], c[:l-1]),
             lcs3(a[:n], b[:m-1], c[:l-1]))


def lcs3_memo(a, b, c):
  n = len(a)
  m = len(b)
  l = len(c)
  if m == 0 or n == 0 or l == 0:
    return 0  

  memo = [[[0 for k in range(l+1)] for j in range(m+1)]for i in range(n+1)]
  for i in range(1, n+1):
    for j in range(1, m+1):
      for k in range(1, l+1):
        if a[i-1] == b[j-1] == c[k - 1]:
          memo[i][j][k] = 1 + memo[i-1][j-1][k-1]
        else:
          memo[i][j][k] = max(memo[i-1][j][k],
                              memo[i][j-1][k],
                              memo[i][j][k-1],
                              memo[i-1][j-1][k],
                              memo[i][j-1][k-1],
                              memo[i-1][j][k-1])
  return memo[n][m][l]

# max(T[i-1][j][k], T[i][j-1][k], T[i][j][k-1],
#                              T[i-1][j-1][k], T[i-1][j][k-1], T[i][j-1][k-1])

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
    print(lcs3_memo(a, b, c))