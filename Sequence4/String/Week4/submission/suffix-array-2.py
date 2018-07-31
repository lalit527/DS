# python3
import sys

def sort_characters(text):
  n = len(text)
  sorted_char_set = sorted(set(text))
  order = [None] * n
  count = [text.count(c) for c in sorted_char_set]
  for i in range(1, len(count)):
    count[i] += count[i - 1]
  for i in range(n - 1, -1, -1):
    index = sorted_char_set.index(text[i])
    count[index] -= 1
    order[count[index]] = i
  return order

def compute_char_klass(text, order):
  n = len(text)
  klass = [None] * n
  klass[order[0]] = 0
  for i in range(1, n):
    if text[order[i]] != text[order[i - 1]]:
      klass[order[i]] = klass[order[i - 1]] + 1
    else:
      klass[order[i]] = klass[order[i - 1]]
  return klass

def sort_doubled(text, L, order, klass):
  n = len(text)
  count = [0] * n
  new_order = [None] * n
  for i in range(n):
    count[klass[i]] += 1 
  for j in range(1, n):
    count[j] += count[j - 1]
  for i in range(n - 1, -1, -1):
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

def build_suffix_array(text):
  order = sort_characters(text)
  klass = compute_char_klass(text, order)
  L = 1
  while L < len(text):
    order = sort_doubled(text, L, order, klass)
    klass = update_klass(order, klass, L)
    L *= 2
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
