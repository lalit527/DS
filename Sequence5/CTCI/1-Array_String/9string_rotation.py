def is_rotation(s1, s2):
  if len(s1) == 0 or len(s1) != len(s2):
    return False
  s1 = s1 + s1
  return _is_substring(s1, s2)

def _is_substring(s1, s2):
  return kmp_pattern(s2, s1)

def kmp_pattern(pattern, text):
  print(pattern, text)
  S = pattern + '$' + text
  s = compute_prefix(S)
  result = []
  for i in range(len(pattern) + 1, len(S)):
    if s[i] == len(pattern):
      result.append(i - 2 * len(pattern))
  return result

def compute_prefix(pattern):
  n = len(pattern)
  s = [None for i in range(n)]
  s[0] = 0
  border = 0
  for i in range(1, n):
    while border > 0 and pattern[i] != pattern[border]:
      border = s[border - 1]
    if pattern[i] == pattern[border]:
      border += 1
    else:
      border = 0
    s[i] = border
  return s

s1 = "waterbottle"
s2 = "erbottlewat"
print(is_rotation(s1, s2))