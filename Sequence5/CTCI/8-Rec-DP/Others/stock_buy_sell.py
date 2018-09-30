def stock_buy_sell(prices, K):
  if K == 0 or prices == []:
    return 0
  
  days = len(prices)
  num_transactions = K + 1 

  T = [[0 for _ in range(days)] for _ in range(num_transactions)]

  for transaction in range(1, num_transactions):
    max_diff = -prices[0]
    for day in range(1, days):
      T[transaction][day] = max(T[transaction][day - 1], prices[day] + max_diff)
      max_diff = max(max_diff, T[transaction - 1][day] - prices[day])
  print_actual_solution(T, prices)
  return T[-1][-1]

def stock_buy_sell_slow(prices, K):
    if K == 0 or prices == []:
      return 0
  
    days = len(prices)
    num_transactions = K + 1 

    T = [[0 for _ in range(days)] for _ in range(num_transactions)]

    for transaction in range(1, num_transactions):
      for day in range(1, days):
        T[transaction][day] = max(T[transaction][day - 1], max([(prices[day] - prices[m] + T[transaction -1][m]) for m in range(days)]))
    print_actual_solution(T, prices)
    return T[-1][-1]

def print_actual_solution(T, prices):
  transaction = len(T) - 1
  day = len(T[0]) - 1
  stack = []
  while True:
    if transaction == 0 or day == 0:
      break
    if T[transaction][day] == T[transaction][day - 1]:
      day -= 1
    else:
      stack.append(day)
      max_diff = T[transaction][day] - prices[day]
      for k in range(day - 1, -1, -1):
        if T[transaction - 1][k] == max_diff:
          stack.append(k)
          transaction -= 1
          break
  
  for entry in range(len(stack) - 1, -1, -2):
    print("Buy on day {day} at price {price}".format(day=stack[entry], prices=prices[stack[transaction]]))
    print("Sell on day {day} at price {price}".format(day=stack[entry], prices=prices[stack[transaction - 1]]))


if __name__ == '__main__':
  prices = [2, 5, 7, 1, 4, 3, 1, 3]
  print(stock_buy_sell_slow(prices, 3))