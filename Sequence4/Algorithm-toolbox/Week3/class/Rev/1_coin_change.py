def min_changes(m):
  coins = [1, 5, 10]
  changes = []
  for coin in coins[::-1]:
    while m >= coin:
      m -= coin
      changes.append(coin)
  return len(changes)



if __name__ == '__main__':
  m = 28
  print(min_changes(m))