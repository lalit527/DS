def is_unique(data):
  """
    Given a string, check if it has unique characters
  """
  char_set = [False for _ in range(128)]

  for c in data:
    val = ord(c)
    if char_set[val]:
      return False
    else:
      char_set[val] = True
  return True

def is_unique_case_ignore(data):
  """
    Given a string, check if it has unique characters
  """
  char_set = [False for _ in range(128)]

  for c in data:
    val = ord(c)
    if val >= 65 and val <= 91:
      if char_set[val] or char_set[val + 32]:
        return False
      else:
        char_set[val] = True
    elif  val >= 97 and val <=123:
      if char_set[val] or char_set[val - 32]:
        return False
      else:
        char_set[val] = True
    elif char_set[val]:
      return False
    else:
      char_set[val] = True
  return True


S = "abcdA"
print(is_unique_case_ignore(S))