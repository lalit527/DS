def optimal_bst(array, freq):
  return _optimal_bst(array, freq, 0, len(array) - 1, 1)

def _optimal_bst(array, freq, low, high, level):
  if low > high:
    return 0
  min_val = float("inf")
  for index in range(low, high + 1):
    val = (_optimal_bst(array, freq, low, index -1, level + 1) + level * freq[index] + _optimal_bst(array, freq, index + 1, high, level + 1))
    min_val = min(min_val, val)
  return min_val

def optimal_bst_dp(array, freq):
  size = rows = cols = len(array)
  T = [[0 for _ in range(cols)] for _ in range(rows)]
  for i in range(rows):
    T[i][i] = freq[i]
  
  for sub_tree in range(2, size + 1):
    for start in range(size + 1 - sub_tree):
      end = start + sub_tree - 1
      T[start][end] = float('inf')
      total = sum(freq[start: end + 1])
      for k in range(start, end + 1):
        val = total + (0 if k - 1 < 0 else T[start][k - 1]) + (0 if k + 1 > end else T[k + 1][end])
        T[start][end] = min(val, T[start][end])
  return T[0][-1]


if __name__ == "__main__":
  array = [10, 12, 16, 21]
  freq = [4, 2, 6, 3]
  print(optimal_bst_dp(array, freq))
  # test