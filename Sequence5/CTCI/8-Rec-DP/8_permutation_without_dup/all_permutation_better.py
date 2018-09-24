from collections import defaultdict

D = defaultdict(lambda: False)

def build_freq_table(s):
  freq_table = defaultdict(lambda: 0)
  for c in s:
    freq_table[c] += 1
  return freq_table 

def get_all_permutation(freq, prefix, remaining, result):
  if remaining == 0:
    result.append(prefix)
    return
  
  for c, count in freq.items():
    if count > 0:
      freq[c] -= 1
      get_all_permutation(freq, prefix + c, remaining - 1, result)
      freq[c] = count

def get_permutation(s):
  result = []
  freq_table = build_freq_table(s)
  get_all_permutation(freq_table, "", len(s), result)
  return result


perm = get_permutation("aaab")
print(perm)