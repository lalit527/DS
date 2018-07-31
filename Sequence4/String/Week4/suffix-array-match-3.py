# python3
import sys

def sort_characters(S):
  n = len(S)
  sort_char_set = sorted(set(S))
  order = [None] * n
  count = [S.count(c) for c in sort_char_set]
  for i in range(1, len(count)):
    count[i] += count[i - 1]
  for i in range(n-1, -1, -1):
    index = sort_char_set.index(S[i])
    count[index] -= 1
    order[count[index]] = i
  return order
  
def compute_char_klass(S, order):
  n = len(S)
  klass = [None] * n
  klass[order[0]] = 0
  for i in range(1, n):
    if S[order[i]] != S[order[i - 1]]:
      klass[order[i]] = klass[order[i - 1]] + 1
    else:
      klass[order[i]] = klass[order[i - 1]]
  return klass

def sort_doubled(S, L, order, klass):
  n = len(S)
  count = [0] * n
  new_order = [None] * n
  for i in range(n):
    count[klass[i]] += 1
  
  for j in range(1, n):
    count[j] += count[j - 1]
  
  for i in range(n-1, -1, -1):
    start = (order[i] - L + n) % n
    cl = klass[start]
    count[cl] = count[cl] - 1
    new_order[count[cl]] = start
  return new_order

def update_klass(new_order, klass, L):
  n = len(new_order)
  new_klass = [None] * n
  new_klass[new_order[0]] = 0
  for i in range(1, n):
    cur = new_order[i]
    prev = new_order[i - 1]
    mid = (cur + L)
    mid_prev = (prev + L) % n
    if klass[cur] != klass[prev] or klass[mid] != klass[mid_prev]:
      new_klass[cur] = new_klass[prev] + 1
    else:
      new_klass[cur] = new_klass[prev]
  return new_klass

def build_suffix_array(S):
  order = sort_characters(S)
  klass = compute_char_klass(S, order)
  L = 1
  while L < len(S):
    order = sort_doubled(S, L, order, klass)
    klass = update_klass(order, klass, L)
    L = 2 * L
  return order

def pattern_matching_suffix_array(text, pattern, suffix_array, occs):
  min_index = 0
  max_index = len(text)
  n = len(text)
  m = len(pattern)
  while min_index < max_index:
    mid_index = (min_index + max_index) // 2
    suffix = text[suffix_array[mid_index]: min(suffix_array[mid_index] + m, n)]
    if pattern > suffix:
      min_index = mid_index + 1
    else:
      max_index = mid_index
  start = min_index
  max_index = len(text)
  while min_index < max_index:
    mid_index = (min_index + max_index) // 2
    suffix = text[suffix_array[mid_index]: min(suffix_array[mid_index] + m, n)]
    if pattern < suffix:
      max_index = mid_index
    else:
      min_index = mid_index + 1
  end = max_index
  if start <= end:
    print(pattern, 's-e', start, end)
    for i in range(start, end):
      occs.add(suffix_array[i])

def find_occurrences(text, patterns):
  occs = set()
  result = build_suffix_array(text + '$')
  print(result)
  for pattern in patterns:
    print(pattern_matching_suffix_array(text + '$', pattern, result, occs))

  print(occs)
  return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))