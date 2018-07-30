# python3
import sys

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

def find_pattern(pattern, text):
  result = []
  S = pattern + '$' + text
  s = compute_prefix(S)
  for i in range(len(pattern) + 1, len(S)):
    if s[i] == len(pattern):
      result.append(i - 2 * len(pattern))
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

