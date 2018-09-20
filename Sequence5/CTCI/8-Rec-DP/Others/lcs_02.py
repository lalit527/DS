def test(sequence1, sequence2):
  n = len(sequence1) - 1
  m = len(sequence2) - 1
  return _test(sequence1, sequence2, n, m)

def _test(sequence1, sequence2, n, m):
  if n <= 0 or m <= 0:
    return 0
  if sequence1[n] == sequence2[m]:
    return 1 + _test(sequence1, sequence2, n - 1, m - 1)
  return max(_test(sequence1, sequence2, n - 1, m), _test(sequence1, sequence2, n, m - 1))

def test_memo(sequence1, sequence2):
  n = len(sequence1) + 1
  m = len(sequence2) + 1
  memo = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(1, n):
    for j in range(1, m):
      if sequence1[i - 1] == sequence2[j - 1]:
        memo[i][j] = 1 + memo[i - 1][j - 1]
      else:
        memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
  return memo[n - 1][m - 1]