# python3
import sys

class SuffixArray:
  def __init__(self, text):
    self.order = self.build_suffix_array(text)

  def sort_characters(self, S):
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

  def compute_char_klass(self, S, order):
    n = len(S)
    klass = [None] * n
    klass[order[0]] = 0
    for i in range(1, n):
      if S[order[i]] != S[order[i - 1]]:
        klass[order[i]] = klass[order[i - 1]] + 1
      else:
        klass[order[i]] = klass[order[i - 1]]
    return klass

  def sort_doubled(self, S, L, order, klass):
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

  def update_klass(self, new_order, klass, L):
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

  def build_suffix_array(self, S):
    string_len = len(S)
    order = self.sort_characters(S)
    klass = self.compute_char_klass(S, order)
    L = 1
    while L < string_len:
      order = self.sort_doubled(S, L, order, klass)
      klass = self.update_klass(order, klass, L)
      L *= 2
    return order

class GenomeAssmbling:
  def __init__(self):
    data = self.read_data()
    genome = self.assemble(data)
    print(genome)
  
  def read_data(self):
    data = list(set(sys.stdin.read().strip().split()))
    # print(data)
    return data
  
  def assemble(self, data):
    cur_idx = 0
    genome = data[0]
    first_data = data[cur_idx]
    while True:
      cur_data = data[cur_idx]
      if len(data) == 1:
        break
      del data[cur_idx]
      cur_idx, overlap = self.find_longest_overlap(cur_data + '$', data)
      genome += data[cur_idx][overlap:]
    cur_idx, overlap = self.find_longest_overlap(data[0] + '$', [first_data])
    if overlap > 0:
      return genome[:overlap]
    else:
      return genome 

  def bwt_from_suffix_array(self, text, order):
    alpha = ['$', 'A', 'C', 'G', 'T']
    n = len(text)
    bwt = [''] * n
    for i in range(n):
      bwt[i] = text[(order[i] + n - 1) % n]
    
    counts = dict()
    starts = dict()
    for char in alpha:
      counts[char] = [0] * (n + 1)
    for i in range(n):
      cur = bwt[i]
      for char, count in counts.items():
        counts[char][i + 1] = counts[char][i]
      counts[cur][i + 1] += 1
    cur_idx = 0
    for char in sorted(alpha):
      starts[char] = cur_idx
      cur_idx += counts[char][n]
    return bwt, starts, counts

  def find_longest_overlap(self, text, patterns, k = 12):
    order = SuffixArray(text).order
    bwt, start, count = self.bwt_from_suffix_array(text, order)
    n = len(text) - 1
    occurence = dict()
    for i, pattern_list in enumerate(patterns):
      pattern = pattern_list[:k]
      top = 0
      bottom = len(bwt) - 1
      cur_idx = len(pattern) - 1
      while top <= bottom:
        if cur_idx >= 0:
          symbol = pattern[cur_idx]
          cur_idx -= 1
          if count[symbol][bottom + 1] - count[symbol][top] > 0:
            top = start[symbol] + count[symbol][top]
            bottom = start[symbol] + count[symbol][bottom + 1] - 1
          else:
            break
        else:
          for j in range(top, bottom + 1):
            if not order[j] in occurence:
              occurence[order[j]] = []
            occurence[order[j]].append(i)
          break
    overlap = 0
    for pos, ilist in sorted(occurence.items()):
      for i in ilist:
        if text[pos:-1] == patterns[i][:n - pos]:
          return i, n - pos
    return i, overlap

if __name__ == '__main__':
  GenomeAssmbling()