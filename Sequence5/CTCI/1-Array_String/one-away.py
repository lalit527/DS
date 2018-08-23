def one_away(s, t):
  n = len(s)
  m = len(t)
  if n == m:
    return one_edit_replace(s, t, n, m)
  elif n - 1 == m:
    return one_edit_insert(s, t, n ,m)
  elif n + 1 == m:
    return one_edit_insert(t, s, m, n)

def one_edit_replace(s, t, n, m):
  allow_replace = True
  for i in range(n):
    if s[i] != t[i]:
      if allow_replace:
        allow_replace = False
      else:
        return False
  return True

def one_edit_insert(s, t, n, m):
  index1 = 0
  index2 = 0
  allow_edit = True
  while index1 < n and index2 < m:
    if s[index1] != t[index2]:
      if allow_edit:
        index1 += 1
        allow_edit = False
      else:
        return False
    else:
      index1 += 1
      index2 += 1
  return True

def one_away_eff(s, t):
  n = len(s)
  m = len(t)
  s1 = s if n > m else t
  s2 = s if m > n else t
  print(s1, s2)
  found_diff = False
  index1 = 0
  index2 = 0
  while index1 < len(s1) and index2 < len(s2):
    if s1[index1] != s2[index2]:
      if found_diff:
        return False
      else:
        found_diff = True
      if len(s1) == len(s2):
        index2 += 1
    else:
      index2 += 1
    index1 += 1
  return True  



s = "pel"
t = "pale"

print(one_away(s, t))