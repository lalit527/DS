# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
  value = 0.
  price = []
  for i in range(len(weights)):
    price.append([values[i], weights[i],  values[i]/ weights[i]])

  n = len(values)
  for i in range(1, n):
    key = price[i]
    j = i - 1
    while j >= 0 and price[j][2] < key[2]:
      price[j + 1] = price[j]
      j -= 1
    price[j + 1] = key

  for i in range(n):
    if capacity >= price[i][1]:
      capacity -= price[i][1]
      value += price[i][0]
    elif capacity > 0:
      value += capacity * price[i][2]
      capacity = 0
      break

  print(price)
  return round(value, 4)


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    capacity = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
