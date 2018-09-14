# Make a burrow wheeler string from a given string
def rotation(text):
  n = len(text)
  _text = text * 2
  result = [_text[i: i + n] for i in range(n)]
  # print(result)
  return result

def bwm(text):
  rotated = rotation(text)
  return sorted(rotated)

def bwt_arr(text):
  n = len(text)
  burrow_wheeler_matrix = bwm(text)
  # print(burrow_wheeler_matrix)
  result = ''.join(burrow_wheeler_matrix[i][n-1] for i in range(n))
  # print(result)
  return result


# Gives original string from bw string
def bwt_inverse(text):
  n = len(text)
  last = [(value, index) for index, value in enumerate(text)]
  first = sorted(last)
  first_to_last = {f: l for f,l in zip(first, last)}
  # print(last)
  # print(first)
  # print(first_to_last)
  result = ''
  current = first[0]
  for i in range(n):
    result += current[0]
    current = first_to_last[current]
  # print(result)
  return result[::-1]



text = 'panamabananas$'
result = bwt_arr(text)
print(result)
new_result = bwt_inverse(result)
print(new_result)