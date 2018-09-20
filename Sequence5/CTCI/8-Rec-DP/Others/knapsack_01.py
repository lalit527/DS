def test(values, weights, W):
  n = len(weights) - 1
  return _test(values, weights, W, n)

def _test(values, weights, W, n):
  if n <= 0 or W <= 0:
    return 0
  if weights[n] > W:
    return _test(values, weights, W, n - 1)
  return max(values[n] + _test(values, weights, W - weights[n], n - 1), _test(values, weights, W, n - 1))


def test_memo(values, weights, W):
  col = W + 1
  row = len(weights) + 1
  memo = [[0 for _ in range(col)] for _ in range(row)]
  for i in range(1, row):
    for j in range(1, col):
      if j < weights[i - 1]:
        memo[i][j] = memo[i - 1][j]
      else:
        memo[i][j] = max(memo[i - 1][j], values[i - 1] + memo[i - 1][j - weights[i - 1]])
  return memo[row-1][col-1]