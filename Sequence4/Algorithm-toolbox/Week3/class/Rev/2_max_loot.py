import sys

def get_optimal_value(capacity, weights, values):
  prices = []
  n = len(weights)
  for i in range(n):
    prices.append([weights[i], values[i], values[i]/weights[i]])
  
  prices.sort(key = lambda x: x[2], reverse = True)
  
  value = 0
  for data in prices:
    print(data)
    if capacity == 0:
      break
    elif capacity >= data[0]:
      capacity -= data[0]
      value += data[1]
    else:
      value += data[2] * capacity
      capacity = 0
  return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
