def longest_palindrom(sequence, index, n):
  if n == 0 or n == 1:
    return n
  if sequence[index] == sequence[n - index - 1]:
    return 2 + longest_palindrom(sequence, index + 1, n - 2)
  return max(longest_palindrom(sequence, index, n - 1), longest_palindrom(sequence, index + 1, n - 1))

def longest_palin(sequence):
  return longest_palindrom(sequence, 0, len(sequence))

def longest_palindrom_dp(sequence):
  n = len(sequence)
  T = [[0 for _ in range(n)] for _ in range(n)]
  for row in range(n):
    T[row][row] = 1
  for substring_len in range(2, n + 1):
    for row in range(n - substring_len + 1):
      col = row + substring_len - 1
      if sequence[row] == sequence[col] and substring_len == 2:
        T[row][col] = 2
      elif sequence[row] == sequence[col]:
        T[row][col] = T[row + 1][col - 1] + 2
      else:
        T[row][col] = max(T[row + 1][col], T[row][col - 1])
  return T[0][n-1]
