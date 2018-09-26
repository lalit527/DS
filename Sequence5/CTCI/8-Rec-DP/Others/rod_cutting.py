def rod_cutting(price, n):
  if n <= 0:
    return 0
  max_val = float('-inf')
  for i in range(n):
    max_val = max(max_val, price[i] + rod_cutting(price, n - i - 1))
  return max_val

def rod_cutting_dp(price, n):
  result = [0] * (n + 1)
  for i in range(1, n + 1):
    max_val = float('-inf')
    for j in range(i):
      max_val = max(max_val, price[j] + result[i - j - 1])
    result[i] = max_val
  return result[n]

price = [1, 5, 8, 9, 10, 17, 17, 20]

print('final', rod_cutting_dp(price, len(price)))

"""
def rod_cut(rods, n):
    if n <= 0:
      return 0
    max_profit = float('-inf')
    for i in range(n):
      max_profit = max(max_profit, rods[i] + rod_cut(rods, n - 1 - i))
    return max_profit

def rod_cut_main(rods):
  n = len(rods)
  return rod_cut(rods, n)

def rod_cut_dp(rods):
  n = len(rods)
  T = [0 for i in range(n + 1)]
  for i in range(1, n + 1):
    max_profit = float('-inf')
    for j in range(i):
      max_profit = max(max_profit, rods[j] + T[i - j - 1])
    T[i] = max_profit
  return T[n]
    

rods = [2, 4, 6, 8, 10]
"""