def countChange(changes, n, coin):
  if coin == 0:
    return 1
  
  if coin < 0:
    return 0

  if coin > 0 and n <= 0:
    return 0
  
  return countChange(changes, n - 1, coin) + countChange(changes, n, coin - changes[n-1])

def countChange_memo(changes, n, coins):
  table = [[0 for i in range(n)] for j in range(coins+1)]

  for i in range(n):
    table[0][i] = 1

  for i in range(1, coins + 1):
    for j in range(n):
      x = table[i - changes[j]][j] if i - changes[j] >= 0 else 0

      y = table[i][j-1] if j >= 1 else 0

      table[i][j] = x + y

  return table[coins][n-1]

def coinChange_memo2(changes, n, coin):
  table = [0 for i in range(coin+1)]

  table[0] = 1

  for i in range(0, n):
    for j in range(changes[i], coin + 1):
      table[j] += table[j - changes[i]]
  
  return table[coin]



change = [1, 2, 3]
n = len(change)
coin = 4
print(coinChange_memo2(change, n, coin))