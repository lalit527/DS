def check_premutation(s1, s2):
  if len(s1) != len(s2):
    return False
  char_count = [0 for _ in range(128)]
  for c in s1:
    val = ord(c)
    char_count[val] += 1
  
  for c in s2:
    val = ord(c)
    if char_count[val] > 0:
      char_count[val] -= 1
    else:
      return False
  
  for value in char_count:
    if value > 0:
      return False
  
  return True
    

S = "ABCDE"
T = "AFDE"

print(check_premutation(S, T))
