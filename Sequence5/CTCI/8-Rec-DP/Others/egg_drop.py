def egg_drop(n, k): 
  if k == 1 or n == 1 or k == 1:
    return k
  min_attempt = float('inf')
  for i in range(1, k + 1):
    min_attempt = min(min_attempt, 1 + max(egg_drop(n - 1, i - 1), egg_drop(n, k - i)))
  return min_attempt

eggs = 2
floors = 10

def egg_drop_dp(n, k):
  rows = n + 1
  cols = k + 1
  T = [[0 for _ in range(cols)] for _ in range(rows)]
  for j in range(1, cols):
    T[1][j] = j
  for i in range(2, rows):
    for j in range(1, cols):
      T[i][j] = min(1 + max(T[i-1][j-1], T[i][cols - j])) 
  return T

print(egg_drop_dp(eggs, floors))