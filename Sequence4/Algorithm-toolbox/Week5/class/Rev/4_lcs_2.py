import sys

def lcs2(s1, s2):
  m = len(s1)
  n = len(s2)
  if m == 0 or n == 0:
    return 0
  
  if s1[m-1] == s2[n-1]:
    return  1 + lcs2(s1[:m-1], s2[:n-1])

  return max(lcs2(s1[:m], s2[:n-1]), lcs2(s1[:m-1], s2[:n]))


def lcs2_memo(s1, s2):
  m = len(s1)
  n = len(s2)
  if m == 0 or n == 0:
    return 0
  memo = [[0 for _ in range(n+1)] for _ in range(m+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      if s1[i - 1] == s2[j - 1]:
        memo[i][j] = memo[i-1][j-1] + 1
      else:
        memo[i][j] = max(memo[i-1][j], memo[i][j-1])
  
  print(memo)
  return memo[m][n]


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

    print(lcs2_memo(a, b))
