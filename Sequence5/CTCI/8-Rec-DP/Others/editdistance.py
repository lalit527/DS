def min_dist(str1, str2, n1, n2):
  if n1 == 0:
    return n2
  if n2 == 0:
    return n1
  if str1[n1 - 1] == str2[n2 - 1]:
    return min_dist(str1, str2, n1-1, n2-1)
  return min(min_dist(str1, str2, n1, n2-1), 
             min_dist(str1, str2, n1-1, n2-1),
             min_dist(str1, str2, n1-1, n2-1))

def test(str1, str2):
  return min_dist(str1, str2, len(str1), len(str2))

def min_dist_dp(str1, str2):
  rows = len(str1) + 1
  cols = len(str2) + 1
  T = [[0 for _ in range(cols)] for _ in range(rows)]
  for i in range(rows):
    T[i][0] = i
  for j in range(cols):
    T[0][j] = j
  for i in range(1, rows):
    for j in range(1, cols):
      if str1[i - 1] == str2[j - 1]:
        T[i][j] = T[i - 1][j - 1]
      else:
        T[i][j] = 1 + min(T[i-1][j-1], T[i-1][j], T[i][j-1])
  return T[rows - 1][cols - 1]
