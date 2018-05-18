import sys

def path(cost, m, n):
  if (m < 0 or n < 0):
    return sys.maxsize
  elif (m == 0 and n == 0):
    return cost[m][n]
  else:
    return cost[m][n] + min(path(cost, m-1, n), path(cost, m, n-1), path(cost, m-1, n-1))

cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(path(cost, 2, 2))