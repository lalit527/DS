def match_naive(text, pattern):
  n = len(text)
  m = len(pattern)
  i = 0
  for i in range(n - m + 1):
    for j in range(m):
      if text[i + j] != pattern[j]:
        break
    
    if j == m - 1:
      print("Pattern found at index", str(i))

pattern = "nana"
text = "pananabananas"
txt = "AABAACAADAABAAABAA"
pat = "AABA"
match_naive(txt, pat)

