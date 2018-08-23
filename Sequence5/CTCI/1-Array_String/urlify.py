def urlify(s):
  n = len(s)
  space_count = 0
  for c in s:
    if c == ' ':
      space_count += 1
  
  index = n + space_count * 2
  char_array = [None] * index
  for i in range(n - 1, -1, -1):
    if s[i] == ' ':
      char_array[index - 1] = '0'
      char_array[index - 2] = '2'
      char_array[index - 3] = '%'
      index -= 3
    else:
      char_array[index - 1] = s[i]
      index -= 1
  return "".join(char_array)


S = "Mr John Smith"
print(urlify(S))
print(S)