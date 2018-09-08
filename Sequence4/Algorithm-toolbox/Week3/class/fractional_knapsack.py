def get_optimal_value(capacity, weights, values):
  n = len(weights)
  data = []
  for i in range(n):
    data.append([weights[i], values[i], values[i]/weights[i]])

  data.sort(key = lambda x: x[2], reverse = True)

  price = 0

  print(data)
  for i in range(n):
    if capacity == 0:
      return price
    if data[i][0] <= capacity:
      capacity -= data[i][0]
      price += data[i][1]
    else:
      price += capacity * data[i][2]
      capacity = 0
  
  print(price)


W = 60
values = [60, 100, 120]
weights = [20, 50, 30]
print(get_optimal_value(W, weights, values))