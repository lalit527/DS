def cut_rod(rod, n):
  return _cut_rod(rod, n - 1)

def _cut_rod(rod, n):
  if n == 0:
    return 0
  max_value = float('-inf')
  for i in range(n):
    max_value = max(max_value, rod[i] + _cut_rod(rod, n - i - 1))
  return max_value

def rod_cut_dp(rod, n):
  length = len(rod)
  T = [0 for _ in range(length + 1)]
  for i in range(1, length + 1):
    max_value = float('-inf')
    for j in range(i):
      max_value = max(max_value, rod[j] + T[i - j - 1])
    T[i] = max_value
  return T[n]

rod = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 9
print(rod_cut_dp(rod, n))