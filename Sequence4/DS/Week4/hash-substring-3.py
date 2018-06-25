# python3

from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_fn(s, p, x):
  _hash = 0
  for c in reversed(s):
    _hash = ((_hash * x + ord(c)) % p + p) % p
  return _hash

def recalculate_hashes(pattern, text, p, x):
  m = len(pattern)
  n = len(text)
  result = [None] * (n - m + 1)
  S = text[n - m : n]
  result[n - m] = hash_fn(S, p, x)

  y = 1
  for i in range(1, m + 1):
    y = (y * x) % p

  for i in range(n - m - 1, -1, -1):
    result[i] = (x * result[i + 1] + ord(text[i]) -y * ord(text[i + m])) % p

  return result

def get_occurrences(pattern, text):
    _prime = 1000000007
    x = randint(0, _prime)
    _hashes = recalculate_hashes(pattern, text, _prime, x)
    result = []
    pat_hs = hash_fn(pattern, _prime, x)
    for i in range(0, len(text) - len(pattern) + 1):
      if pat_hs != _hashes[i]:
        continue
      if text[i:i + len(pattern)] == pattern:
        result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

