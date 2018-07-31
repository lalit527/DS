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
  print(s)
  return s

def kmp_pattern(pattern, text):
  S = pattern + '$' + text
  s = compute_prefix(S)
  result = []
  for i in range(len(pattern) + 1, len(S)):
    if s[i] == len(pattern):
      result.append(i - 2 * len(pattern))
  return result

if __name__ == "__main__":
  pattern = "abra"
  text = "abracadabra"
  print(kmp_pattern(pattern, text))