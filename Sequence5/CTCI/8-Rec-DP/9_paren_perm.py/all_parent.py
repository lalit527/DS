def insert_inside(string, left_index):
  left = string[:left_index + 1]
  right = string[left_index + 1:]
  return left + "()" + right

def generate_paren(remaining):
  s = set()
  if remaining == 0:
    s.add("")
  else:
    prev = generate_paren(remaining - 1)
    for string in prev:
      for i in range(len(string)):
        if string[i] == '(':
          new = insert_inside(string, i)
          s.add(new)
      s.add("()" + string)
  return s


result = generate_paren(3)
print(result)