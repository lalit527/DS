def lcs(s1, s2):
  return _lcs(s1, s2, len(s1), len(s2))

def _lcs(s1, s2, n, m):
  if n <= 0 or m <= 0:
    return 0
    return n
  if s1[n - 1] == s2[m - 1]:
    return 1 + _lcs(s1, s2, n - 1, m - 1)
  return max(_lcs(s1, s2, n - 1, m), _lcs(s1, s2, n, m - 1))

def lcs_dp(s1, s2):
  n = len(s1)
  m = len(s2)
  T = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
  for i in range(n + 1):
    T[i][0] = i
  for j in range(m + 1):
    T[0][j] = j
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if s1[i - 1] == s2[j - 1]:
        T[i][j] = T[i - 1][j - 1] + 1
      else:
        T[i][j] = max(T[i - 1][j], T[i][j - 1])
  return T
  
s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
print(lcs(s1, s2))