def get_permutation(s):
  if s is None:
    return None
  n = len(s)
  permutations = []
  if n == 0:
    permutations.append("")
    return permutations
  
  for i in range(n):
    before = s[0: i]
    after = s[i + 1: n]
    partials = get_permutation(before + after)
    for p in partials:
      permutations.append(s[i] + p)
  return permutations




perm = get_permutation("abcd")
print(perm)