def get_permutation(s):
  permutations = []
  _get_permutations("", s, permutations)
  return permutations

def _get_permutations(prefix, string, results):
  if len(string) == 0:
    results.append(prefix)
  else:
    n = len(string)
    for i in range(n):
      before = string[0: i]
      after = string[i + 1: n]
      c = string[i]
      _get_permutations(prefix + c, before + after, results)

perm = get_permutation("abcd")
print(perm)