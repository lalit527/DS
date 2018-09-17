def min_egg_drop(n, k):
  if n == 1 or k == 0:
    return k
  
  min_val = float("inf")
  for i in range(1, k + 1):
    min_val = min(min_val, 1 + max(min_egg_drop(n - 1, i - 1), min_egg_drop(n, k-i)))

  return min_val


def min_egg_drop_memo(n, k):
  if n == 1 or k == 0:
    return k
  memo = [[j if i == 1 else 0 for j in range(k+1)] for i in range(n+1)]
  for i in range(2, n+1):
    for j in range(1, k+1):
      memo[i][j] = float("inf")
      for k in range(1, j + 1):
        res = 1 + max(memo[i-1][k-1], memo[i][j - k])
        if res < memo[i][j]:
          memo[i][j] = res

  print(memo)

# for egg in range(2, num_eggs):
#         for floor in range(1, num_floors):
#             T[egg][floor] = min(1 + max(T[egg - 1][k - 1], T[egg][floor - k]) for k in range(1, floor + 1))
  
# for i in range(2, n+1): 
#         for j in range(2, k+1): 
#             eggFloor[i][j] = INT_MAX 
#             for x in range(1, j+1): 
#                 res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
#                 if res < eggFloor[i][j]: 
#                     eggFloor[i][j] = res 

n = 2
k = 10

print(min_egg_drop_memo(n, k))