def rec_mult(a, b):
  bigger = a if a > b else b
  smaller = b if a > b else a
  return _rec_mult(smaller, bigger)

def _rec_mult(smaller, bigger):
  if smaller == 0:
    return 0
  elif smaller == 1:
    return bigger
  
  s = smaller >> 1
  side1 = rec_mult(s, bigger)
  side2 = side1
  if smaller % 2 == 1:
    side2 = _rec_mult(smaller - s, bigger)
  return side1 + side2


print(rec_mult(8, 9))