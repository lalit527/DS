def cod_cutting(rod, n):
  if n == 0:
    return 0
  max_value = 0
  for i in range(n):
    max_value = max(max_value, rod[i] + cod_cutting(rod, n - 1 - i))
  return max_value

def rod_cutting_dp(rod):
  n = len(rod)
  T = [0 for _ in range(n + 1)]
  for i in range(1, n+1):
    max_value = 0
    for j in range(i):
      max_value = max(max_value, rod[j] + T[i - j - 1])
    T[i] = max_value
  return T[n]


price = [1, 5, 8, 9, 10, 17, 17, 20]

print('final', rod_cutting_dp(price))

