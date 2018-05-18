def allPath(m, n):
  if (m == 1 or n == 1):
    return 1

  return allPath(m-1, n) + allPath(m, n-1)
def all_path_memo(m, n):
  result = [[0 for x in range(m)] for y in range(n)]
  return _all_path_memo(m, n, result)

def _all_path_memo(m, n, result):
  for i in range(m):
    result[i][0] = 1
  for i in range(n):
    result[0][i] = 1

  for i in range(1, m):
    for j in range(1, n):
      result[i][j] = result[i-1][j] + result[i][j-1]
  return result[m-1][n-1]

def main():
  print(all_path_memo(3, 3))

if __name__ == '__main__':
  main()  