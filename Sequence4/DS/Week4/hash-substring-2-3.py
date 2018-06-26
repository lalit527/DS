# python3

from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(P, p, x):
  _hash = 0
  n = len(P)
  for i in range(n-1, -1, -1):
    _hash = ((_hash * x + ord(P[i])) % p + p) % p
  return _hash

def precompute_hash(text, pattern, p, x):
  m = len(pattern)
  n = len(text)
  H = [None] * (n - m + 1)
  S = text[n - m: n]
  print(S)
  H[n - m] = poly_hash(S, p, x)
  y = 1
  for i in range(1, m + 1):
    y = (y * x) % p
  print(y)
  for i in range(n - m - 1, -1, -1):
    H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + m])) % p
  print(H)
  return H

def get_occurrences(pattern, text):
    _prime = 1000000007
    x = randint(0, _prime)
    result = []
    pHash = poly_hash(pattern, _prime, x)
    H = precompute_hash(text, pattern, _prime, x)

    for i in range(len(text) - len(pattern) + 1):
      if pHash != H[i]:
        continue
      if text[i: i + len(pattern)] == pattern:
        result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

