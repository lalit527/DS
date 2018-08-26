def check_palin_perm(s):
  s = s.lower()
  char_count = [0 for _ in range(26)]
  for c in s:
    val = ord(c) - 97
    if val >= 0 and val < 26:
      char_count[val] += 1
  has_one_odd = False
  for count in char_count:
    if count % 2 == 1:
      if has_one_odd:
        return False
      else:
        has_one_odd = True
  return True

def check_palin_perm_opt(s):
  s = s.lower()
  char_count = [0 for _ in range(26)]
  odd_count = 0
  for c in s:
    val = ord(c) - 97
    if val >= 0 and val < 26:
      char_count[val] += 1
      if char_count[val] % 2 == 1:
        odd_count += 1
      else:
        odd_count -= 1
  return odd_count <= 1

S = "Tact Coa"
print(check_palin_perm_opt(S))
