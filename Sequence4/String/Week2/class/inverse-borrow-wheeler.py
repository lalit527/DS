def inverse_bwt(bwt):
  last = [(value, index) for (index, value) in enumerate(bwt)]
  print(last)
  first = sorted(last)
  print(first)
  first_to_last = {f: l for f, l in zip(first, last)}
  next = first[0]
  result = ''
  print(first_to_last)
  for i in range(len(bwt)):
    result += next[0]
    next = first_to_last[next]
  print(result)
  return result[::-1]

if __name__ == '__main__':
  bwt = 'smnpbnnaaaaa$a'
  print(inverse_bwt(bwt))