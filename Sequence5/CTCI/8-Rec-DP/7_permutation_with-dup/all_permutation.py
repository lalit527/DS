def get_permutation(s):
  if s is None:
    return None

  permutations = []
  if len(s) == 0:
    permutations.append("")
    return permutations
  
  first = s[0]
  remainder = s[1:]
  words = get_permutation(remainder)
  for word in words:
    for i in range(len(word) + 1):
      s = insert_char(word, first, i)
      permutations.append(s)
  return permutations

def insert_char(word, first, i):
  strat = word[:i]
  end = word[i:]
  return strat + first + end



perm = get_permutation("abcd")
print(perm)