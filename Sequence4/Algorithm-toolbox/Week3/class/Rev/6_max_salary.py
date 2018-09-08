import sys

def largest_number_fixed(a):
  res = []
  _largest_number_fixed(a, res)
  return ''.join(map(lambda x: str(x), res))

def is_current_better(a, b):
  if str(a) + str(b) >= str(b) + str(a):
    return a
  else:
    return b

def _largest_number_fixed(a, res):
  if len(a) == 0:
    return res

  _max = 0
  _index = -1
  for i, d in enumerate(a):
    if is_current_better(_max, d):
      _max = d
      _index = i
  
  res.append(_max)
  a.pop(_index)
  _largest_number_fixed(a, res)
  

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number_fixed(a))