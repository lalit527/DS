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
  half_product = rec_mult(s, bigger)
  if smaller % 2 == 0:
    return half_product + half_product
  else:
    return half_product + half_product + bigger

print(rec_mult(8, 9))