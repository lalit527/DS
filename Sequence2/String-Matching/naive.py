def search(pat, txt):
  return bfsm(txt, len(txt), pat, len(pat))

def bfsm(text, n, pattern, m):
  for i in range(0, n-m+1):
    j = 0
    while (j < m and pattern[j] == text[i+j]):
      j += 1
    if j == m:
      return i
  return -1

txt = "AABAACAADAABAAABAA"
pat = "AABA"
print(search (pat, txt))