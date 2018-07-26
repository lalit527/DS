def sort_characters(S):
  n = len(S)
  sorted_char = sorted(set(S))
  order = [None] * n
  count = [S.count(c) for c in sorted_char]
  for i in range(1, len(count)):
    count[i] += count[i - 1]
  for i in range(n - 1, -1, -1):
    index = sorted_char.index(S[i])
    count[index] -= 1
    order[count[index]] = i
  return order

def compute_char_klass(S, order):
  n = len(S)
  klass = [None] * n
  klass[order[0]] = 0
  for i in range(1, n):
    if S[order[i]] != S[order[i - 1]]:
      klass[order[i]] = klass[order[i-1]] + 1
    else:
      klass[order[i]] = klass[order[i-1]]
  return klass

def sort_doubled(S, L, order, klass):
  n = len(S)
  count = [0] * n
  newOrder = [None] * n
  for i in range(n):
    count[klass[i]] = count[klass[i]] + 1
  for j in range(1, n):
    count[j] = count[j] + count[j - 1]
  for i in range(n-1, -1, -1):
    start = (order[i] - L + n) % (n)
    cl = klass[start]
    count[cl] = count[cl] - 1
    newOrder[count[cl]] = start
  return newOrder

def update_klass(newOrder, klass, L):
  n = len(newOrder)
  new_klass = [None] * n
  new_klass[newOrder[0]] = 0
  for i in range(1, n):
    cur = newOrder[i]
    prev = newOrder[i - 1]
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

def main():
  S = "AACGATAGCGGTAGA$"
  print(build_suffix_array(S))

if __name__ == "__main__":
  main()