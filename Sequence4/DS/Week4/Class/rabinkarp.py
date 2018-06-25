class PatternMatching:
  def __init__(self, prime=101):
    self.prime = prime

  def pattern_matching(self, text, pattern):
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(paterrm, m - 1)
    text_hash = create_hash(text, m - 1)

    for i in range(1, n - m + 2):
      if pattern_hash == text_hash:
        if check_equal(text[i - 1: i + m-1], pattern[0:]):
          return i - 1
        
        if i < n - m + 1:
          text_hash = recalculate_hash(text, i - 1, i + m-1, text_hash, m)
    return -1

  def check_equal(str1, str2):
    if len(str1) != len(str2):
      return False
    for i, j in zip(str1, str2):
      if i != j:
        return False
    return True

  def create_hash(input, end):
    hash = 0
    for i in range(end + 1):
      hash = hash + ord(input[i])*pow(self.prime, i)
    return hash

  def recalculate_hash(input, old_index, new_index, old_hash, pattern_len):
    new_hash = old_hash - ord(input[old_index])
    new_hash = new_hash / prime
    new_hash += ord(input[new_hash]) * pow(prime, pattern_len - 1)
    return new_hash

    
P = PatternMatching()
print(P.prime)


# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_func(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = ((ans * x + ord(c)) % p + p) % p
    return ans

def precompute_hashes(pattern, text, p, x):
    result = [None] * (len(text) - len(pattern) + 1)
    S = text[(len(text)-len(pattern)):len(text)]
    result[len(text)-len(pattern)] = hash_func(S, p, x)

    y = 1
    for i in range(1, len(pattern) + 1):
        y = (y * x) % p
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        result[i] = (x * result[i+1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % p

    return result

def get_occurrences(pattern, text):
    _prime = 1000000007
    x = random.randint(0, _prime)
    hashes = precompute_hashes(pattern, text, _prime, x)
    result = []
    pHash = hash_func(pattern, _prime, x)
    for i in range(0, len(text) - len(pattern) + 1):
        if pHash != hashes[i]:
            continue
        if text[i:i+ len(pattern)] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
