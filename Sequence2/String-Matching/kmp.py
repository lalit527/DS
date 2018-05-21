def computeLPS(pat, m, lps):
  len = 0
  lps[0]
  i = 1
  while i < m:
    if pat[i] == pat[len]:
      len += 1
      lps[i] = len
      i += 1
    else:
      if len != 0:
        len = lps[len - 1]
      else:
        lps[i] = 0
        i += 1

def KMPSearch(pat, txt):
  m = len(pat)
  n = len(txt)
  lps = [0]*m
  j = 0
  computeLPS(pat, m, lps)
  i = 0 


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)