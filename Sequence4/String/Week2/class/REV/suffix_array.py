def create_suffix_array(text):
  n = len(text)
  suffixes = []
  for i in range(n):
    suffixes.append((text[i:], i))
  sorted_suffixes = sorted(suffixes, key = lambda x: x[0])
  result = [i for text, i in sorted_suffixes]
  return result

def pattern_matching_suffix_array(pattern, text, suffixes):
  n = len(text)
  min_index = 0
  max_index = n
  while min_index < max_index:
    mid_index = (min_index + max_index) // 2
    if pattern > text[suffixes[mid_index]]:
      min_index = mid_index + 1
    else:
      max_index = mid_index - 1

  start = min_index
  max_index = n
  while min_index < max_index:
    mid_index = (min_index + max_index) // 2
    if pattern > text[suffixes[mid_index]]:
      min_index = mid_index + 1
    else:
      max_index = mid_index - 1


text = "panamabananas$"
pattern = "ana"
s_a = create_suffix_array(text)
print(s_a)