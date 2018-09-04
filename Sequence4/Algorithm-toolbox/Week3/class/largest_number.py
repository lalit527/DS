def largest_combination(num):
  num = str(num)
  digit = []
  _largest_combination(num, digit)
  return int(''.join(map(lambda x: str(x), digit)))

def _largest_combination(num, digit):
  if num:
    index, d = largest(num)
    digit.append(d)
    num = update(num, index)
    _largest_combination(num, digit)
    

def update(num, index):
  n = len(num)
  return num[0:index] + num[index+1:]

def largest(num):
  _max = -1
  index = -1
  for i, c in enumerate(num):
    if int(c) > _max:
      _max = int(c)
      index = i
  return index, _max

print(largest_combination(537919))
