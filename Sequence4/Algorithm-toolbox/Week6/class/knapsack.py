def knapsack_rep_memo(W, n, val, wt):
  value = [0 for i in range(W + 1)]
  for i in range(W+1):
    for j in range(n):
      if wt[j] <= i:
        value[i] = max(value[i], value[i - wt[j]] + val[j])
  return value[W]
    

def knapsack_rep_rec(W, n, val, wt):
  if W == 0 or n == 0:
    return 0
  max_wt = float('-inf')
  for i in range(n):
    if wt[i] <= W:
      num_wt = knapsack_rep_rec(W - wt[i], n, val, wt) + val[i]
    if num_wt > max_wt:
      max_wt = num_wt
  return max_wt

def knapsack_rec(W, n, val, wt):
  if W == 0 or n == 0:
    return 0
  if wt[n-1] > W:
    return knapsack_rep_rec(W, n-1, val, wt)

  return max(val[n-1] + knapsack_rep_rec(W - val[n-1], n-1, val, wt),
              knapsack_rep_rec(W, n-1, val, wt))
    

def knapsack_memo(W, n, val, wt):
  if W == 0 or n == 0:
    return 0
  cols = W + 1
  rows = n + 1
  value = [[0 for i in range(cols)] for j in range(rows)]
  for i in range(1, rows):
    for j in range(1, cols):
      if wt[i - 1] <= j:
        value[i][j] = max(value[i-1][j], value[i-1][j - wt[i-1]] + val[i-1])
      else:
        value[i][j] = value[i-1][j]
  print(value)
  return value[rows - 1][cols - 1]


# W = 100
# val = [10, 30, 20] 
# wt = [5, 10, 15] 
# n = len(val) 
  
# print(knapsack_rep_rec(W, n, val, wt)) 

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapsack_memo(W , n , val , wt))
  