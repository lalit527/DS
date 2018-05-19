import sys

def path(cost, m, n):
  if (m < 0 or n < 0):
    return sys.maxsize
  elif (m == 0 and n == 0):
    return cost[m][n]
  else:
    return cost[m][n] + min(path(cost, m-1, n), path(cost, m, n-1), path(cost, m-1, n-1))


def path_memo(cost, m, n):
  result = [[0 for x in range(m+1)] for y in range(n+1)]
  result[0][0] = cost[0][0]
  for i in range(1, m+1):
    result[i][0] = result[i-1][0] + cost[i][0]

  for j in range(1, n+1):
    result[0][j] = result[0][j-1] + cost[0][j]

  for i in range(1, m+1):
    for j in range(1, n+1):
      result[i][j] = min(result[i-1][j], result[i][j-1], result[i-1][j-1]) + cost[i][j]

  return result[m][n]

cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(path_memo(cost, 2, 2))